from sqlalchemy.orm import Session
from models.admin import Admin


class AdminService:
    def __init__(self, db: Session):
        self.db = db

    def add_admin(self, admin_login: str, admin_password: str):
        new_admin = Admin(
            admin_login=admin_login,
            admin_password=admin_password,
        )
        self.db.add(new_admin)
        self.db.commit()
        self.db.refresh(new_admin)
        return new_admin

    def get_all_admins(self):
        admins = self.db.query(Admin).all()
        return admins

    def get_admin_by_details(self, admin_login: str, admin_password: str):
        admin = self.db.query(Admin).filter(Admin.admin_login == admin_login, Admin.admin_password == admin_password).first()
        return admin
