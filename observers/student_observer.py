from observers.observer import Observer
from database.mongodb import MongoDB

db = MongoDB().get_db()

class StudentObserver(Observer):
    def __init__(self, student):
        self.student = student

    def update(self, notice):

        notification = {

            "student_name": self.student["name"],
            "student_email": self.student["email"],

            "organization": notice["organization"],
            "classroom": notice["classroom"],

            "teacher": notice["teacher"],

            "title": notice["title"],
            "message": notice["message"],

            "status": "unread"
        }

        db.notifications.insert_one(notification)

        print(f"Notification sent to {self.student['name']}")