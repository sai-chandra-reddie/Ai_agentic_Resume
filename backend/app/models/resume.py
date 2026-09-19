import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB

from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    user_id = Column(String, nullable=True, index=True)
    filename = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    storage_path = Column(String, nullable=True)
    status = Column(String, nullable=False, default="pending")
    extracted_text = Column(Text, nullable=True)
    parsed_profile = Column(JSONB, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
