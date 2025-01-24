from sqlalchemy.orm import Session
from models.room import Room


class RoomService:
    def __init__(self, db: Session):
        self.db = db

    def add_room(self, room_genre: str, room_price: int):
        new_room = Room(room_genre=room_genre,
                        room_price=room_price)
        self.db.add(new_room)
        self.db.commit()
        self.db.refresh(new_room)
        return new_room