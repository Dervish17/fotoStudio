from sqlalchemy.orm import Session

from models.client import Client
from models.employee import Employee
from models.order import Order
from models.room import Room


class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def add_order(self, client_id: int, employee_id: int, room_id: int, order_date: str, order_status: str):
        new_order = Order(client_id=client_id,
                          employee_id=employee_id,
                          room_id=room_id,
                          order_date=order_date,
                          order_status=order_status)

        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def all_orders(self):
        orders = self.db.query(Order.order_id,
                               Client.client_name,
                               Client.client_surname,
                               Employee.employee_name,
                               Room.room_name,
                               Order.order_date,
                               Order.order_status).join(Client).join(Employee).join(Room).all()
        return orders

    def delete_order(self, order_id):
        with self.db.begin():
            order_to_delete = self.db.query(Order).get(order_id)
            if order_to_delete:
                self.db.delete(order_to_delete)

    def update_order(self, order_id: int, client_id: int, employee_id: int, room_id: int, order_date: str,
                     order_status: str):
        order = self.db.query(Order).filter(Order.order_id == order_id).first()
        try:
            if order:
                order.client_id = client_id
                order.employee_id = employee_id
                order.room_id = room_id
                order.order_date = order_date
                order.order_status = order_status
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
