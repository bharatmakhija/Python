from abc import ABC, abstractmethod

class AbstractUser(ABC):

    user_count = 0

    @classmethod
    def get_user_id(cls):
        cls.user_count += 1
        return cls.user_count


    def __init__(self):
        self.id = self.get_user_id()
        self.name = None
        self.phone = None
        self.email = None
        super().__init__()

    @abstractmethod
    def create_user(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone


class User(AbstractUser):

    def __init__(self):
        super().__init__()


    def create_user(self, name, email, phone=None):
        super().create_user(name,email,phone)

    @classmethod
    def get_user_from_str(cls, user_str):
        name, email, phone = user_str.split('-')
        user = cls()
        user.create_user(name,email,phone)
        return user

    def __str__(self):
        return "id: {}, name: {}, email: {}, phone: {}".format(self.id, self.name, self.email, self.phone)