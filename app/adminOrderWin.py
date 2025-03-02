from PyQt6.QtCore import QDateTime
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QDateTimeEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QMessageBox

from database import SessionLocal
from services.order_services import OrderService
from services.client_service import ClientService
from services.employee_services import EmployeeService
from services.room_services import RoomService


class AddAdminOrder(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.data = data
        self.initUI()
        if self.data:
            self.upload_editable_data()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.resize(600, 600)
        self.setWindowTitle('Запись на съемку')
        self.setWindowIcon(QIcon('resources/12.png'))

        style = """QPushButton {
                                        font-size: 16px; 
                                        background-color: #ffb8c6; 
                                        color: black; 
                                        border: none; 
                                        padding: 10px; 
                                        border-radius: 5px;
                                    }
                                    QPushButton:hover {
                                        background-color: #f0768b;
                                    }
                                    QPushButton:pressed {
                                        background-color: #ddadaf;
                                    }
                    QLabel {font: 15pt Monotype Corsiva; color: white;
                    }
                    QLineEdit{border: 1px solid white; padding: 5px; font: 12pt Monotype Corsiva; color: white;
                    }
                    QDateTimeEdit{font: 12pt Monotype Corsiva; color: white;}
                    QComboBox{font: 12pt Monotype Corsiva; color: white;
                    }
                                """
        name_label = QLabel("Укажите имя:")
        name_label.setStyleSheet(style)
        self.text_name = QLineEdit()
        self.text_name.setMaxLength(50)
        self.text_name.setPlaceholderText("Введите имя")
        self.text_name.setStyleSheet(style)

        surname_label = QLabel("Укажите фамилию:")
        surname_label.setStyleSheet(style)
        self.text_surname = QLineEdit()
        self.text_surname.setMaxLength(50)
        self.text_surname.setPlaceholderText("Введите фамилию")
        self.text_surname.setStyleSheet(style)

        tel_label = QLabel("Укажите телефон:")
        tel_label.setStyleSheet(style)
        self.text_tel = QLineEdit()
        self.text_tel.setMaxLength(50)
        self.text_tel.setPlaceholderText("Введите телефон")
        self.text_tel.setStyleSheet(style)

        # email_label = QLabel("Укажите имейл:")
        # email_label.setStyleSheet(style)
        # self.text_email = QLineEdit()
        # self.text_email.setMaxLength(50)
        # self.text_email.setPlaceholderText("Введите имейл")
        # self.text_email.setStyleSheet(style)

        employee_label = QLabel("Выберите фотографа:")
        employee_label.setStyleSheet(style)
        self.employee_combo = QComboBox()
        self.employee_combo.setStyleSheet(style)
        self.employee_combo.addItems(self.names_employees())

        room_label = QLabel("Выберите  комнату:")
        room_label.setStyleSheet(style)
        self.room_combo = QComboBox()
        self.room_combo.setStyleSheet(style)
        self.room_combo.addItems(self.get_room())

        label_session_datetime = QLabel("Укажите дату и время фотосъемки:")
        label_session_datetime.setStyleSheet(style)
        self.session_datetime = QLineEdit(QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss'))
        self.session_datetime.setStyleSheet(style)

        status_label = QLabel("Статус заявки:")
        status_label.setStyleSheet(style)
        self.status_combo = QComboBox()
        self.status_combo.setStyleSheet(style)
        self.status_combo.addItems(['Активна', 'Отменена'])

        self.button_update = QPushButton('Изменить')
        self.button_update.setStyleSheet(style)
        self.button_update.clicked.connect(self.update_order)
        self.button_update.setFont(QFont('Monotype Corsiva'))

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet(style)
        self.button_cancel.clicked.connect(self.cancellation)
        self.button_cancel.setFont(QFont('Monotype Corsiva'))

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_update)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.text_name)
        main_layout.addWidget(surname_label)
        main_layout.addWidget(self.text_surname)
        main_layout.addWidget(tel_label)
        main_layout.addWidget(self.text_tel)
        # main_layout.addWidget(email_label)
        # main_layout.addWidget(self.text_email)
        main_layout.addWidget(employee_label)
        main_layout.addWidget(self.employee_combo)
        main_layout.addWidget(room_label)
        main_layout.addWidget(self.room_combo)
        main_layout.addWidget(label_session_datetime)
        main_layout.addWidget(self.session_datetime)
        main_layout.addWidget(status_label)
        main_layout.addWidget(self.status_combo)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def names_employees(self):
        db = SessionLocal()
        employee_service = EmployeeService(db)
        return employee_service.get_names_employees()

    def get_room(self):
        db = SessionLocal()
        room_service = RoomService(db)
        return room_service.room_names()

    def update_order(self):
        name = self.text_name.text()
        surname = self.text_surname.text()
        tel = self.text_tel.text()
        # email = self.text_email.text()
        employee_name = self.employee_combo.currentText()
        session_datetime = self.session_datetime.text()
        status = self.status_combo.currentText()

        # if not name.strip() or not surname.strip() or not tel.strip() or not email.strip():
        #     QMessageBox.information(self, "Ошибка", "Заполните все поля!")
        #     return
        db = SessionLocal()
        order_service = OrderService(db)
        client_service = ClientService(db)
        employee_service = EmployeeService(db)
        room_service = RoomService(db)
        room_id = room_service.get_room_id_by_name(
            f"{self.room_combo.currentText().split(' ')[0]} {self.room_combo.currentText().split(' ')[1]}")
        client = client_service.get_client_id_by_name(name, surname, tel)
        try:
            order_service.update_order(order_id=self.order_id,
                                       client_id=client.client_id,
                                       room_id=room_id,
                                       employee_id=employee_service.get_employee_id_by_name(employee_name),
                                       order_date=session_datetime,
                                       order_status=status)
            QMessageBox.information(self, "Успех", "Запись на съемку изменена!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении заявки: {str(e)}")
            print(e)

    def get_client(self):
        db = SessionLocal()
        client_service = ClientService(db)
        client = client_service.get_client_by_name(self.data[1].split(' ')[0], self.data[1].split(' ')[1])
        return client

    def upload_editable_data(self):
        self.order_id = self.data[0]
        self.text_name.setText(self.data[1].split(' ')[0])
        self.text_surname.setText(self.data[1].split(' ')[1])
        self.employee_combo.setCurrentText(self.data[2])
        self.room_combo.setCurrentText(self.data[3])
        self.session_datetime.setText(self.data[4])
        self.status_combo.setCurrentText(self.data[5])

    def cancellation(self):
        self.close()
