from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, nullable=False)
    equipment_id = Column(Integer, ForeignKey('equipments.equipments_id'))

    equipment = relationship('Equipment', back_populates='equipment')
    order = relationship('Order', back_populates='employee')