from factories.university_factory import UniversityFactory
from factories.college_factory import CollegeFactory


class FactoryProvider:

    @staticmethod
    def get_factory(organization: str):

        organization = organization.lower()

        if organization == "university":
            return UniversityFactory()

        elif organization == "college":
            return CollegeFactory()

        raise ValueError("Invalid organization")