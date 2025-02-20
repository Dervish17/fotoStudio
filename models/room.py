from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, nullable=False)
    room_genre = Column(String, nullable=False)

    order = relationship('Order', back_populates='room')