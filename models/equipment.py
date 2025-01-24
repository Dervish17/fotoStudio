from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Equipment(Base):
    __tablename__ = 'equipments'

    equipment_id = Column(Integer, primary_key=True, index=True)
    equipment_type = Column(String, nullable=False)
    equipment_status = Column(String, nullable=False)
    equipment_condition = Column(String, nullable=False)

    employee = relationship('Employee', back_populates='equipment')
    order = relationship('Order', back_populates='equipment')