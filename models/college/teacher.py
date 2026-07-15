from models.user import User


class CollegeTeacher(User):

    def __init__(
        self,
        name,
        email,
        password,
        department
    ):
        super().__init__(
            name,
            email,
            password,
            "teacher",
            "college"
        )

        self.department = department
        self.organization = "college"