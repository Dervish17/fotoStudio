from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_surname = Column(String, nullable=False)
    client_tel = Column(String, nullable=False)
    client_email = Column(String, nullable=False)

    order = relationship('Order', back_populates='client')