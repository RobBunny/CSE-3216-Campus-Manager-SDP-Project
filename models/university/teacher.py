from models.user import User


class UniversityTeacher(User):

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
            "university"
        )

        self.department = department
        self.organization = "university"