from fastapi import APIRouter
from database.mongodb import MongoDB
from schemas.notice_schema import NoticeRequest
from services.notice_service import NoticeService
from services.notification_service import NotificationService

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

@router.get("/notifications/unread-count/{email}")
def get_unread_count(email: str):

    count = db.notifications.count_documents(
        {
            "student_email": email,
            "status": "unread"
        }
    )

    return {
        "unread_count": count
    }

@router.patch("/notifications/read/{email}")
def mark_notifications_as_read(email: str):

    result = db.notifications.update_many(

        {
            "student_email": email,
            "status": "unread"
        },

        {
            "$set": {
                "status": "read"
            }
        }

    )

    return {

        "message": "Notifications marked as read",

        "updated_notifications": result.modified_count

    }