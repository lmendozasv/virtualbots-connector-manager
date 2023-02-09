
from sqlalchemy import Column, Integer, String, DateTime
from db.declarative_base import Base


class ChatLogger(Base):
    __tablename__ = 'chat_logger'
    id = Column(Integer, primary_key=True)
    caller = Column(String)
    dt_created = Column(DateTime)
    payload = Column(String)
