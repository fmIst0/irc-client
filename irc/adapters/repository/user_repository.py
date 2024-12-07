from irc.port.user_port import UserPort


class UserRepository(UserPort):
    def register_user(self, username: str, password: str):
        pass

    def set_username(self, user_id: int, new_username: str):
        pass
