from sqlalchemy.orm import Session
from models.room import Room


class RoomService:
    def __init__(self, db: Session):
        self.db = db

    def add_room(self, room_name: str, room_genre: str):
        new_room = Room(room_name=room_name,
                        room_genre=room_genre)
        self.db.add(new_room)
        self.db.commit()
        self.db.refresh(new_room)
        return new_room

    def get_rooms(self):
        rooms = self.db.query(Room).all()
        return rooms

    def room_names(self):
        room_names = [room.room_name for room in self.get_rooms()]
        return room_names

    def get_room_id_by_name(self, name):
        room = self.db.query(Room).filter(Room.room_name == name).first()
        return room.room_id
