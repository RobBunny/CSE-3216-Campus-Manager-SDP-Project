from models.user import User

class UniversityStudent(User):

    def __init__(
        self,
        name,
        email,
        password,
        student_id,
        classroom
    ):

        super().__init__(
            name,
            email,
            password,
            "student",
            "university"
        )

        self.student_id = student_id
        self.classroom = classroom