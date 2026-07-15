from database.mongodb import MongoDB

db = MongoDB().get_db()


class UserService:

    @staticmethod
    def register(user):

        data = vars(user)

        # Example:
        # UniversityTeacher -> university_teachers
        # CollegeStudent -> college_students

        ROLE_COLLECTIONS = {
            "teacher": "teachers",
            "student": "students",
            "staff": "staff"
        }

        collection_name = (
            f"{user.organization}_"
            f"{ROLE_COLLECTIONS[user.role]}"
        )

        db[collection_name].insert_one(data)

        return {
            "message": "Registration successful",
            "saved_to": collection_name
        }