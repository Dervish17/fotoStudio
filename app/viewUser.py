from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from app.addClientWin import AddClient
from database import SessionLocal
from services.room_services import RoomService

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

        rooms = self.get_all_rooms()

        self.image_labels = []
        self.buttons = []

        for room in rooms:
            image_label = QLabel()
            pixmap = QPixmap(room.room_path)
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
            button.clicked.connect(lambda _, r_id=room.room_id, r_name=room.room_name: self.book_photo(r_id, r_name))
            button.setFont(QFont('Monotype Corsiva'))
            self.buttons.append(button)

            item_layout = QVBoxLayout()
            item_layout.addWidget(image_label)
            item_layout.addWidget(button)

            photos_layout.addLayout(item_layout)

        main_layout.addLayout(photos_layout)
        self.setLayout(main_layout)

    def get_all_rooms(self):
        db = SessionLocal()
        rooms = RoomService(db).get_rooms()
        return rooms

    def book_photo(self, room_id, room_name):
        self.book = AddClient(room_id, room_name)
        self.book.show()
