from models.user import User


class UniversityStaff(User):

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
            "university"
        )

        self.designation = designation
        self.organization = "university"