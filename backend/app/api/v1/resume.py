import os
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeUploadResponse
from app.api.deps import get_current_user
from app.models.user import User


router = APIRouter()

ALLOWED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
]
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "uploads")


@router.post("/upload", response_model=ResumeUploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type. Allowed: PDF, DOC, DOCX. Got: {file.content_type}",
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large. Max size is {MAX_FILE_SIZE_MB}MB.",
        )

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_id = uuid.uuid4()
    ext = os.path.splitext(file.filename or "resume")[1]
    storage_filename = f"{file_id}{ext}"
    storage_path = os.path.join(UPLOAD_DIR, storage_filename)

    with open(storage_path, "wb") as f:
        f.write(contents)

    now = datetime.now(timezone.utc)
    resume = Resume(
        id=file_id,
        user_id=str(current_user.id),

        filename=file.filename,
        file_type=file.content_type,
        storage_path=storage_path,
        status="pending",
        extracted_text=None,        
        parsed_profile=None,        
        created_at=now,
        updated_at=now,
    )
    db.add(resume)
    await db.flush()   

    return resume
