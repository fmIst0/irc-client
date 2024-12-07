from abc import ABC, abstractmethod


class UserPort(ABC):
    @abstractmethod
    async def register_user(self, username: str, password: str):
        pass

    @abstractmethod
    async def set_username(self, user_id: int, new_username: str):
        pass
