from pydantic import BaseModel

class NoticeRequest(BaseModel):
    organization: str      # university / college
    classroom: str         # CSE-221
    title: str
    message: str
    teacher: str