from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Portfolio contact messages collection
class Message(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)

# Optional: simple schema to showcase projects if needed later
class Project(BaseModel):
    title: str
    description: str
    tags: List[str] = []
    url: Optional[str] = None
    repo: Optional[str] = None
