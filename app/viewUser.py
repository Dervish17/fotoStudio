from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox)

class ViewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.setWindowTitle('Выбор фильма')
        self.setGeometry(300, 200, 800, 500)
        self.setWindowIcon(QIcon('resources/12.png'))

        main_layout = QVBoxLayout()

        photos_layout = QHBoxLayout()

        self.image_labels = []
        self.buttons = []

        photo_paths = [
            "resources/1.jpg",
            "resources/2.jpg",
            "resources/3.jpg",
            "resources/4.jpg",
            "resources/5.jpg",
        ]

        for path in photo_paths:
            image_label = QLabel()
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(250, 400)
            image_label.setPixmap(pixmap)
            self.image_labels.append(image_label)

            button = QPushButton("Забронировать")
            button.setStyleSheet("""
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
            """)
            button.clicked.connect(lambda _, p=path: self.book_photo(p))
            button.setFont(QFont('Monotype Corsiva'))
            self.buttons.append(button)

            item_layout = QVBoxLayout()
            item_layout.addWidget(image_label)
            item_layout.addWidget(button)

            photos_layout.addLayout(item_layout)

        main_layout.addLayout(photos_layout)
        self.setLayout(main_layout)

    def book_photo(self, photo_path):
       # self.book = AddFilm()
       # self.book.show()
        pass
