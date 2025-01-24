from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    order_status = Column(String, nullable=False)
    order_date = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    room_id = Column(Integer, ForeignKey('rooms.room_id'))
    equipment_id = Column(Integer, ForeignKey('equipments.equipment_id'))

    employee = relationship('Employee', back_populates='order')
    room = relationship('Room', back_populates='order')
    equipment = relationship('Equipment', back_populates='order')