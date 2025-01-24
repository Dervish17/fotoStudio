from sqlalchemy.orm import Session

from models.employee import Employee
from models.equipment import Equipment
from models.order import Order
from models.room import Room


class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def add_order(self, order_status: str, order_date: int, employee_id: int, room_id: int, equipment_id: int):
        new_order = Order(order_status=order_status,
                          order_date=order_date,
                          employee_id=employee_id,
                          room_id=room_id,
                          equipment_id=equipment_id)
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def all_orders(self):
        orders = self.db.query(Order.order_id,
                               Order.order_status,
                               Employee.employee_name,
                               Room.room_name,
                               Equipment.equipment_type).join(Employee).join(Room).join(Equipment).all()
        return orders
