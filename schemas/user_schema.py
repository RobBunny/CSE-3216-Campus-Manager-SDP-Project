from pydantic import BaseModel
from typing import Optional


class RegisterRequest(BaseModel):

    name: str
    email: str
    password: str
    organization: str
    role: str

    department: Optional[str] = None
    student_id: Optional[str] = None
    designation: Optional[str] = None
    classroom: Optional[str] = None