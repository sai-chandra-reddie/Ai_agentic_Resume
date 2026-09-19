from fastapi import APIRouter, UploadFile, File, HTTPException, status

router = APIRouter()

ALLOWED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type. Allowed types are: PDF, DOC, DOCX. Got: {file.content_type}"
        )
    
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File is too large. Max size is {MAX_FILE_SIZE_MB}MB"
        )
    

    await file.seek(0)
    
    return {
        "message": "Resume uploaded and validated successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents)
    }
