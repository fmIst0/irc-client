from abc import ABC, abstractmethod


class ChannelPort(ABC):
    @abstractmethod
    async def create_channel(self, name: str):
        pass

    @abstractmethod
    async def join_channel(self, channel_id: int):
        pass

    @abstractmethod
    async def get_channel_metadata(self, channel_id: int):
        pass
