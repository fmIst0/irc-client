from irc.port.user_port import UserPort


class UserUseCase:
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    async def register_user(self, username: str, password: str):
        return self.user_port.register_user(username, password)

    async def set_username(self, user_id: int, new_username: str):
        return self.user_port.set_username(user_id, new_username)
