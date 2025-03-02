from PyQt6.QtCore import QDateTime
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QDateTimeEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QMessageBox

from database import SessionLocal
from services.client_service import ClientService
from app.reservWin import AddOrder
from app.oldClientWin import OldClient


class AddClient(QWidget):
    def __init__(self, room_id=None, room_name=None):
        super().__init__()

        self.room_id = room_id
        self.room_name = room_name
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.resize(600, 600)
        self.setWindowTitle('Добавление клиента')
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

        tel_label = QLabel("Укажите свой телефон:")
        tel_label.setStyleSheet(style)
        self.text_tel = QLineEdit()
        self.text_tel.setMaxLength(50)
        self.text_tel.setPlaceholderText("Введите телефон")
        self.text_tel.setStyleSheet(style)

        email_label = QLabel("Укажите свой имейл:")
        email_label.setStyleSheet(style)
        self.text_email = QLineEdit()
        self.text_email.setMaxLength(50)
        self.text_email.setPlaceholderText("Введите имейл")
        self.text_email.setStyleSheet(style)


        self.button_add = QPushButton('Добавить и перейти к заказу')
        self.button_add.setStyleSheet(style)
        self.button_add.clicked.connect(self.add_client)
        self.button_add.setFont(QFont('Monotype Corsiva'))

        self.continue_button = QPushButton('Я являюсь клиентом')
        self.continue_button.setStyleSheet(style)
        self.continue_button.clicked.connect(self.continue_add)
        self.continue_button.setFont(QFont('Monotype Corsiva'))

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet(style)
        self.button_cancel.clicked.connect(self.cancellation)
        self.button_cancel.setFont(QFont('Monotype Corsiva'))

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.continue_button)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.text_name)
        main_layout.addWidget(surname_label)
        main_layout.addWidget(self.text_surname)
        main_layout.addWidget(tel_label)
        main_layout.addWidget(self.text_tel)
        main_layout.addWidget(email_label)
        main_layout.addWidget(self.text_email)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def add_client(self):
        name = self.text_name.text()
        surname = self.text_surname.text()
        tel = self.text_tel.text()
        email = self.text_email.text()

        if not name or not surname or not tel or not email:
            QMessageBox.critical(self, 'Ошибка', 'Не все поля заполнены!')
            return
        db = SessionLocal()
        client_service = ClientService(db)
        client = client_service.add_client(name, surname, tel, email)

        if client:
            QMessageBox.information(self, 'Успех', 'Клиент успешно добавлен!')
            self.book = AddOrder(self.room_id, self.room_name, client)
            self.book.show()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Произошла ошибка при добавлении клиента!')

    def continue_add(self):
        self.book_with_old_client = OldClient(self.room_id, self.room_name)
        self.book_with_old_client.show()

    def cancellation(self):
        self.close()