from database.mongodb import MongoDB

db = MongoDB().get_db()


class NotificationService:

    @staticmethod
    def get_notifications(email):
        notifications = list(
            db.notifications.find(
                {"student_email": email},
                {"_id": 0}
            )
        )

        return notifications

    @staticmethod
    def get_unread_count(email):

        count = db.notifications.count_documents({
            "student_email": email,
            "status": "unread"
        })

        return {
            "unread_count": count
        }

    @staticmethod
    def mark_all_as_read(email):

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
            "updated": result.modified_count
        }