from lld.split_wise_app.models.user import User


class UserService:
    all_users = {}

    def add_user(self, id, name, email):
        user = User(name=name, id=id, email=email)
        self.__class__.all_users[id] = user
        return user

