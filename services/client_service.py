from sqlalchemy.orm import Session
from models.client import Client


class ClientService:
    def __init__(self, db: Session):
        self.db = db

    def add_client(self, client_name: str, client_surname: str, client_tel: str, client_email: str):
        new_client = Client(client_name=client_name,
                            client_surname=client_surname,
                            client_tel=client_tel,
                            client_email=client_email)
        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)
        return new_client

    def get_all_clients(self):
        clients = self.db.query(Client).all()
        return clients

    def get_client_id_by_name(self, name, surname, tel):
        client = self.db.query(Client).filter(Client.client_name == name,
                                              Client.client_surname == surname,
                                              Client.client_tel == tel).first()
        if client:
            return client
        return None

    def get_client_by_details(self, name, surname, tel):
        client = self.db.query(Client).filter(Client.client_name == name,
                                              Client.client_surname == surname,
                                              Client.client_tel == tel).first()
        return client

    def get_client_by_name(self, name, surname):
        client = self.db.query(Client).filter(Client.client_name == name,
                                              Client.client_surname == surname).all()
        return client
