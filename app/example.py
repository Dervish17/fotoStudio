import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, images_path):
        super().__init__()

        self.images = list(Path(images_path).glob("*.jpg"))
        if not self.images:
            raise FileNotFoundError(f"No images found in {images_path}")
        self.current_image = self.images[0]

        # Создаем лейбл для отображения фотографии
        self.image_label = QLabel()
        self.set_image(0)

        # Кнопки для перехода к следующей/предыдущей фотографии
        self.prev_button = QPushButton("<")
        self.next_button = QPushButton(">")
        self.book_button = QPushButton("Забронировать")

        # Обработчики событий для кнопок
        self.prev_button.clicked.connect(self.show_prev_image)
        self.next_button.clicked.connect(self.show_next_image)
        self.book_button.clicked.connect(self.open_booking_window)

        # Компоновка элементов интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.book_button)
        self.setLayout(layout)

        self.setWindowTitle("Просмотр фотозон")

    def set_image(self, index):
        pixmap = QPixmap(str(self.images[index]))
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.width(), self.image_label.height(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio
        ))

    def show_prev_image(self):
        current_index = self.images.index(self.current_image)
        new_index = (current_index - 1) % len(self.images)
        self.set_image(new_index)
        self.current_image = self.images[new_index]

    def show_next_image(self):
        current_index = self.images.index(self.current_image)
        new_index = (current_index + 1) % len(self.images)
        self.set_image(new_index)
        self.current_image = self.images[new_index]

    def open_booking_window(self):
        print(f"Бронирование зоны для фото: {self.current_image.name}")
        # Здесь можно реализовать открытие нового окна для бронирования


if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        main_window = MainWindow("../resources")  # Указать путь к папке с фотографиями
        main_window.show()
        sys.exit(app.exec())
    except FileNotFoundError as e:
        print(e)