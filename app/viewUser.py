from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox)


class ViewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.setWindowTitle('Выбор фотозоны')
        self.resize(800, 800)
        self.setWindowIcon(QIcon('resources/12.png'))

        main_layout = QVBoxLayout()

        photos_layout = QHBoxLayout()

        photo_paths = [
            "resources/1.jpg",
            "resources/2.jpg",
            "resources/3.jpg",
            "resources/4.jpg",
            "resources/5.jpg",
        ]

        for path in photo_paths:
            item_widget = QWidget()
            item_layout = QVBoxLayout(item_widget)

            image_label = QLabel()
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(250, 400)
            image_label.setPixmap(pixmap)

            button = QPushButton("Забронировать")
            button.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    background-color: white;
                    color: black;
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
            button.clicked.connect(lambda _, p=path: self.book_photo(p))

            item_layout.addWidget(image_label)
            item_layout.addWidget(button)
            photos_layout.addWidget(item_widget)

        main_layout.addLayout(photos_layout)
        self.setLayout(main_layout)

    def book_photo(self, photo_path):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Бронирование")
        msg_box.setText(f"Вы выбрали фотографию: {photo_path}")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setStyleSheet("background-color: white; color: black;")
        msg_box.exec()
