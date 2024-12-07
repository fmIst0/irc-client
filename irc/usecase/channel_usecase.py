from irc.port.channel_port import ChannelPort


class ChannelUseCase:
    def __init__(self, channel_port: ChannelPort):
        self.channel_port = channel_port

    async def create_channel(self, name: str):
        return self.channel_port.create_channel(name)

    async def join_channel(self, channel_id: int):
        return self.channel_port.join_channel(channel_id)

    async def get_channel_metadata(self, channel_id: int):
        return self.channel_port.get_channel_metadata(channel_id)
