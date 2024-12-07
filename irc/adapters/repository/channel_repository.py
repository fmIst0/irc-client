from irc.port.channel_port import ChannelPort


class ChannelRepository(ChannelPort):
    async def create_channel(self, name: str):
        pass

    async def join_channel(self, channel_id: int):
        pass

    async def get_channel_metadata(self, channel_id: int):
        pass
