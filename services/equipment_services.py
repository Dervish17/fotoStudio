from sqlalchemy.orm import Session
from models.equipment import Equipment


class EquipmentService:
    def __init__(self, db: Session):
        self.db = db

    def add_equipment(self, equipment_type: str, equipment_status: str, equipment_condition: str):
        new_equipment = Equipment(equipment_type=equipment_type,
                                  equipment_status=equipment_status,
                                  equipment_condition=equipment_condition)
        self.db.add(new_equipment)
        self.db.commit()
        self.db.refresh(new_equipment)
        return new_equipment