from irc.port.message_port import MessagePort


class MessageRepository(MessagePort):
    async def send_message(self, user_id: int, channel_id: int, content: str):
        pass

    async def list_messages(self, channel_id: int):
        pass
