from abc import ABC

class User(ABC):

    def __init__(
        self,
        name,
        email,
        password,
        role,
        organization
    ):

        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.organization = organization