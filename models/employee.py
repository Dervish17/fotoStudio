from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, nullable=False)
    employee_post = Column(String, nullable=False)
    employee_tel = Column(String, nullable=False)

    order = relationship('Order', back_populates='employee')