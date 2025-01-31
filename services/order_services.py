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

    def delete_order(self, order_id):
        with self.db.begin():
            order_to_delete = self.db.query(Order).get(order_id)
            if order_to_delete:
                self.db.delete(order_to_delete)

    def update_order(self, order_id: int, order_status: str,
                         order_date: int, employee_id: int, room_id: int, equipment_id: int):
        order = self.db.query(Order).filter(Order.order_id == order_id).first()
        try:
            if order:
                order.order_status = order_status
                order.order_date = order_date
                order.employee_id = employee_id
                order.room_id = room_id
                order.equipment_id = equipment_id
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)