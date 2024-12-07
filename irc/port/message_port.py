from abc import ABC, abstractmethod


class MessagePort(ABC):
    @abstractmethod
    async def send_message(self, user_id: int, channel_id: int, content: str):
        pass

    @abstractmethod
    async def list_messages(self, channel_id: int):
        pass
