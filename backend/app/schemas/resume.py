from pydantic import BaseModel
from typing import Optional, List


class ResumeBase(BaseModel):
    title: str
    summary: Optional[str] = None
    skills: List[str] = []


class ResumeCreate(ResumeBase):
    pass


class ResumeResponse(ResumeBase):
    id: str

    class Config:
        from_attributes = True
