from sqlalchemy.orm import Session
from models.employee import Employee


class EmployeeService:
    def __init__(self, db: Session):
        self.db = db

    def add_employee(self, employee_name: str, equipment_id: int):
        new_employee = Employee(employee_name=employee_name,
                                equipment_id=equipment_id)
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee
