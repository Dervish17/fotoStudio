from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication)
from PyQt6.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #90e6e4;")
        self.setWindowTitle('Фотостудия "Фото"')
        self.resize(300, 400)
        self.setWindowIcon(QIcon('resources/54544.png'))

        picture_label = QLabel()
        pixmap = QPixmap('resources/54544.png')
        picture_label.setPixmap(pixmap)

        central_widget = QWidget()

        label = QLabel('Войти как')
        label.setStyleSheet("QLabel {font: 24pt Arial; color: black; font-weight: bold;}")
        self.admin_btn = QPushButton('Администратор')
        self.user_btn = QPushButton('Пользователь')

        button_style = """QPushButton {
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
                            }"""
        self.admin_btn.setStyleSheet(button_style)
        self.user_btn.setStyleSheet(button_style)

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
        main_l.addWidget(self.admin_btn)
        main_l.addWidget(self.user_btn)
        main_l.addStretch()

        central_widget.setLayout(main_l)
        self.setCentralWidget(central_widget)

        # self.admin_btn.clicked.connect(self.show_admin_auth)
        # self.user_btn.clicked.connect(self.show_win_user)

    # def show_admin_auth(self):
    #     self.auth = AuthWindow()
    #     self.auth.show()

    # def show_win_user(self):
    #     self.show_user = ViewCinemaUser()
    #     self.show_user.show()

    def closeEvent(self, event):
        QApplication.quit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()