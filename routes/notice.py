from fastapi import APIRouter
from database.mongodb import MongoDB
from schemas.notice_schema import NoticeRequest
from services.notice_service import NoticeService

router = APIRouter()
db = MongoDB().get_db()

@router.post("/notice")
def post_notice(request: NoticeRequest):

    notice = {

        "organization": request.organization,

        "classroom": request.classroom,

        "teacher": request.teacher,

        "title": request.title,

        "message": request.message
    }

    return NoticeService.publish_notice(notice)

@router.get("/notifications/{email}")
def get_notifications(email: str):

    notifications = list(

        db.notifications.find(

            {
                "student_email": email
            },

            {
                "_id": 0
            }

        )

    )

    return notifications