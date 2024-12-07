from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class DBUser(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username})>"


class DBChannel(Base):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    messages = relationship("Message", back_populates="channel")

    def __repr__(self):
        return f"<Channel(name={self.name})>"


class DBMessage(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id"), nullable=False
    )

    user = relationship("User", back_populates="messages")
    channel = relationship("Channel", back_populates="messages")

    def __repr__(self):
        return f"<Message(content={self.content}, timestamp={self.timestamp})>"
