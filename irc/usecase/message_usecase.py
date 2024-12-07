from irc.port.message_port import MessagePort


class MessageUseCase:
    def __init__(self, message_port: MessagePort):
        self.message_port = message_port

    async def send_message(self, user_id: int, channel_id: int, content: str):
        return self.message_port.send_message(user_id, channel_id, content)

    async def list_messages(self, channel_id: int):
        return self.message_port.list_messages(channel_id)
