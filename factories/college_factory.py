from factories.abstract_user_factory import AbstractUserFactory

from models.college.teacher import CollegeTeacher
from models.college.student import CollegeStudent
from models.college.staff import CollegeStaff


class CollegeFactory(AbstractUserFactory):

    def create_teacher(
        self,
        name,
        email,
        password,
        department
    ):
        print("College Factory -> Creating College Teacher")

        return CollegeTeacher(
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
        print("College Factory -> Creating College Student")

        return CollegeStudent(
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
        print("College Factory -> Creating College Staff")

        return CollegeStaff(
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