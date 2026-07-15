from abc import ABC, abstractmethod

class AbstractUserFactory(ABC):

    @abstractmethod
    def create_teacher(
        self,
        name,
        email,
        password,
        department
    ):
        pass

    @abstractmethod
    def create_student(
        self,
        name,
        email,
        password,
        student_id,
        classroom
    ):
        pass

    @abstractmethod
    def create_staff(
        self,
        name,
        email,
        password,
        designation
    ):
        pass

    @abstractmethod
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
        pass