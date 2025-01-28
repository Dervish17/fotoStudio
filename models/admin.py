from sqlalchemy import Column, Integer, String
from database import Base


class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True, index=True)
    admin_login = Column(String, nullable=False)
    admin_password = Column(String, nullable=False)