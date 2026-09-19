from datetime import datetime
from typing import Optional, Any
from uuid import UUID

from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    id: UUID
    user_id: Optional[str] = None
    filename: str
    file_type: str
    storage_path: Optional[str] = None
    status: str
    extracted_text: Optional[str] = None
    parsed_profile: Optional[Any] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
