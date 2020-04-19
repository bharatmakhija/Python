from abc import ABC

class AbstractGroup(ABC):

    def __init__(self):
        self.group_id = None
        self.users_list = None


class Group(AbstractGroup):

    group_id_count = 0

    @classmethod
    def get_group_id(cls):
        cls.group_id_count += 1
        return cls.group_id_count

    def __init__(self):
        super().__init__()
        self.group_id = self.get_group_id()


    def __str__(self):
        return "group_id : {} ".format(self.group_id)

    @classmethod
    def get_group_for_users(cls,users_list):
        group = cls()
        group.users_list = users_list
        return group