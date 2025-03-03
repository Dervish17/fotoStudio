from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QMessageBox
from app.reservWin import AddOrder
from database import SessionLocal
from services.client_service import ClientService


class OldClient(QWidget):
    def __init__(self, room_id, room_name):
        super().__init__()
        self.room_id = room_id
        self.room_name = room_name
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.resize(600, 600)
        self.setWindowTitle('Выбор')
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
        label = QLabel('Введите ваши данные:')
        label.setStyleSheet(style)
        self.text_name = QLineEdit()
        self.text_name.setMaxLength(50)
        self.text_name.setPlaceholderText("Введите имя")
        self.text_name.setStyleSheet(style)

        self.text_surname = QLineEdit()
        self.text_surname.setMaxLength(50)
        self.text_surname.setPlaceholderText("Введите фамилию")
        self.text_surname.setStyleSheet(style)

        self.text_tel = QLineEdit()
        self.text_tel.setMaxLength(50)
        self.text_tel.setPlaceholderText("Введите телефон")
        self.text_tel.setStyleSheet(style)

        self.button_add = QPushButton('Далее')
        self.button_add.setStyleSheet(style)
        self.button_add.setFont(QFont('Monotype Corsiva'))

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet(style)
        self.button_cancel.setFont(QFont('Monotype Corsiva'))

        self.button_add.clicked.connect(self.add_order)
        self.button_cancel.clicked.connect(self.cancellation)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(self.text_name)
        main_layout.addWidget(self.text_surname)
        main_layout.addWidget(self.text_tel)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def add_order(self):
        db = SessionLocal()
        client_service = ClientService(db)

        client = client_service.get_client_by_details(self.text_name.text(),
                                                      self.text_surname.text(),
                                                      self.text_tel.text())
        if client:
            self.book = AddOrder(self.room_id, self.room_name, client)
            self.book.show()
        else:
            QMessageBox.information(self, 'Ошибка', 'Клиент с такими данными не найден')

    def cancellation(self):
        self.close()
