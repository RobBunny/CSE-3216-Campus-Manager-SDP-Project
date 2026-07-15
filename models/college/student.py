from models.user import User

class CollegeStudent(User):

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
            "college"
        )

        self.student_id = student_id
        self.classroom = classroom