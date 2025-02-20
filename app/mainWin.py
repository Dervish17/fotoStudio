from PyQt6.QtWidgets import (QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication)
from PyQt6.QtGui import QIcon, QPixmap, QFont
from app.authWindow import AuthWindow
from app.viewUser import ViewUser
# from app.userWin1 import UserWin


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.setWindowTitle('Фотостудия "Narcissus"')
        self.resize(300, 400)
        self.setWindowIcon(QIcon('resources/12.png'))

        picture_label = QLabel('Фотостудия ')
        label = QLabel('Narcissus')
        picture_label.setStyleSheet("QLabel {font: 24pt Monotype Corsiva; color: white; font-weight: bold;}")
        label.setStyleSheet("QLabel {font: 30pt Embassy BT; color: pink; font-weight: bold;}")

        central_widget = QWidget()

        self.user_btn = QPushButton('Пользователь')
        button_style = """
                            QPushButton {
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
                        """
        self.user_btn.setStyleSheet(button_style)
        self.user_btn.setFont(QFont('Monotype Corsiva'))
        self.admin_btn = QPushButton('Администратор')
        self.admin_btn.setStyleSheet('QPushButton {font: 15pt Monotype Corsiva; color: grey; padding: 8px; '
                                     'border-radius: 5px;}')


        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()

        h_l1.addStretch(2)
        h_l1.addWidget(label, 1)
        h_l1.addStretch(2)
        h_l2.addStretch()
        h_l2.addWidget(picture_label)
        h_l2.addStretch()

        main_l.addStretch()
        main_l.addLayout(h_l2)
        main_l.addLayout(h_l1)
        main_l.addWidget(self.user_btn)
        main_l.addStretch()
        main_l.addWidget(self.admin_btn)

        central_widget.setLayout(main_l)
        self.setCentralWidget(central_widget)

        self.admin_btn.clicked.connect(self.show_admin_auth)
        self.user_btn.clicked.connect(self.show_win_user)

    def show_admin_auth(self):
        self.auth = AuthWindow()
        self.auth.show()

    def show_win_user(self):
        self.show_user = ViewUser()
        self.show_user.show()

    def closeEvent(self, event):
        QApplication.quit()
