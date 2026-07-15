from factories.abstract_user_factory import AbstractUserFactory
from models.university.teacher import UniversityTeacher
from models.university.student import UniversityStudent
from models.university.staff import UniversityStaff

class UniversityFactory(AbstractUserFactory):

    def create_teacher(
        self,
        name,
        email,
        password,
        department
    ):
        print("University Factory -> Creating University Teacher")

        return UniversityTeacher(
            name,
            email,
            password,
            department
        )

    def create_student(
        self,
        name,
        email,
        password,
        student_id,
        classroom
    ):
        print("University Factory -> Creating University Student")

        return UniversityStudent(
            name,
            email,
            password,
            student_id,
            classroom
        )

    def create_staff(
        self,
        name,
        email,
        password,
        designation
    ):
        print("University Factory -> Creating University Staff")

        return UniversityStaff(
            name,
            email,
            password,
            designation
        )
    
    def create_user(
        self,
        role,
        name,
        email,
        password,
        department=None,
        student_id=None,
        designation=None,
        classroom=None
    ):

        role = role.lower()

        if role == "teacher":
            return self.create_teacher(
                name,
                email,
                password,
                department
            )

        elif role == "student":
            return self.create_student(
                name,
                email,
                password,
                student_id,
                classroom
            )

        elif role == "staff":
            return self.create_staff(
                name,
                email,
                password,
                designation
            )

        raise ValueError("Invalid role")