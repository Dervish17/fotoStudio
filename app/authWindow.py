from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QMessageBox)

# from app.adminInterfaceWin import AdminInterface
# from database import init_db, SessionLocal
# from services.admins_services import AdminService


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.setWindowTitle('Авторизация')
        self.resize(500, 400)
        self.setWindowIcon(QIcon('resources/54544.png'))

        authorization_label = QLabel('Авторизация')
        authorization_label.setStyleSheet('font: 24pt Monotype Corsiva; color: grey; font-weight: bold;')

        login_label = QLabel('Логин:')
        login_label.setStyleSheet('font: 15pt Monotype Corsiva; color: white; font-weight: bold;')
        password_label = QLabel('Пароль:')
        password_label.setStyleSheet('font: 15pt Monotype Corsiva; color: white; font-weight: bold;')

        self.login = QLineEdit()
        self.login.setStyleSheet("QLineEdit {color: black; background-color: white; padding: 8px; "
                                 "border-radius: 5px; font: 12pt Monotype Corsiva;}")
        self.login.setPlaceholderText('Введите логин')

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setStyleSheet(
            "QLineEdit {color: black; background-color: white; padding: 8px; border-radius: 5px; "
            "font: 12pt Monotype Corsiva;}")
        self.password.setPlaceholderText('Введите пароль')

        self.enter_btn = QPushButton('Войти')
        self.enter_btn.setStyleSheet(
            """
                    QPushButton {
                        font-size: 16px; 
                        background-color: white; 
                        color: black; 
                        border: none; 
                        padding: 10px; 
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: grey;
                    }
                    QPushButton:pressed {
                        background-color: #3c3c3c;
                    }
                """)
        self.enter_btn.setFont(QFont('Monotype Corsiva'))
        self.back_btn = QPushButton('Назад')
        self.back_btn.setStyleSheet('QPushButton {font: 12pt Monotype Corsiva; color: grey; padding: 8px; '
                                    'border-radius: 5px;}')
        self.back_btn.setIcon(QIcon('resources/Back Button.png'))

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l3 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        h_l5 = QHBoxLayout()

        h_l1.addStretch(1)
        h_l1.addWidget(login_label, 1)
        h_l1.addWidget(self.login, 2)
        h_l1.addStretch(2)
        h_l2.addStretch(1)
        h_l2.addWidget(password_label, 1)
        h_l2.addWidget(self.password, 2)
        h_l2.addStretch(2)
        h_l3.addStretch(2)
        h_l3.addWidget(self.enter_btn, 1)
        h_l3.addStretch(2)
        h_l4.addStretch()
        h_l4.addWidget(authorization_label)
        h_l4.addStretch()
        h_l5.addWidget(self.back_btn)
        h_l5.addStretch()

        main_l.addLayout(h_l5)
        main_l.addStretch()
        main_l.addLayout(h_l4)
        main_l.addLayout(h_l1)
        main_l.addLayout(h_l2)
        main_l.addLayout(h_l3)
        main_l.addStretch()

        self.setLayout(main_l)

        self.back_btn.clicked.connect(self.go_back)
        # self.enter_btn.clicked.connect(self.enter)

    # def enter(self):
    #     init_db()
    #     db = SessionLocal()
    #     admin_service = AdminService(db)
    #     admins = admin_service.get_all_admins()
    #     for admin in admins:
    #         if admin.admin_login == self.login.text() and admin.admin_password == self.password.text():
    #             self.enter_admin = AdminInterface()
    #             self.enter_admin.show()
    #         else:
    #             msg_box = QMessageBox()
    #             msg_box.setWindowTitle("Ошибка")
    #             msg_box.setText("Неправильные данные для входа!")
    #             msg_box.setIcon(QMessageBox.Icon.Information)
    #             msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    #             msg_box.setStyleSheet("background-color: white; color: black;")
    #             msg_box.exec()

    # def keyPressEvent(self, event):
    #     if event.key() == 16777220:
    #         self.enter()

    def go_back(self):
        self.close()
