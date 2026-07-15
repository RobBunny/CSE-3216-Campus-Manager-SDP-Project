from database.mongodb import MongoDB
from observers.classroom_notice_board import ClassroomNoticeBoard
from observers.student_observer import StudentObserver

db = MongoDB().get_db()

class NoticeService:

    @staticmethod
    def publish_notice(notice):

        # Save the notice
        db.classroom_notices.insert_one(notice)

        board = ClassroomNoticeBoard()

        # Select the correct student collection
        collection_name = f"{notice['organization']}_students"

        # Only students from the same classroom
        students = db[collection_name].find({
            "classroom": notice["classroom"]
        })

        # Subscribe matching students
        for student in students:
            board.attach(StudentObserver(student))

        # Notify them
        board.post_notice(notice)

        return {
            "message": "Notice Published Successfully"
        }