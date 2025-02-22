from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    room_id = Column(Integer, ForeignKey('rooms.room_id'))
    order_date = Column(String, nullable=False)
    order_status = Column(String, nullable=False)

    employee = relationship('Employee', back_populates='order')
    room = relationship('Room', back_populates='order')
    client = relationship('Client', back_populates='order')
