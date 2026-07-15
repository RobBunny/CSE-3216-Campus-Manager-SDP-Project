from models.user import User


class CollegeStaff(User):

    def __init__(
        self,
        name,
        email,
        password,
        designation
    ):
        super().__init__(
            name,
            email,
            password,
            "staff",
            "college"
        )

        self.designation = designation
        self.organization = "college"