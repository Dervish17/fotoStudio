from sqlalchemy.orm import Session
from models.employee import Employee


class EmployeeService:
    def __init__(self, db: Session):
        self.db = db

    def add_employee(self, employee_name: str, employee_post: str, employee_tel: str):
        new_employee = Employee(employee_name=employee_name,
                                employee_post=employee_post,
                                employee_tel=employee_tel)
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_all_employees(self):
        employees = self.db.query(Employee).all()
        return employees
