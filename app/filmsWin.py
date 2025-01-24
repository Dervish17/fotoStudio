from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from database import init_db, SessionLocal
from services.film_service import FilmService

class FilmWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_db = init_db()
        db = SessionLocal()
        self.film_service = FilmService(db)
        self.add_names()

    def initUI(self):
        self.resize(400, 300)
        self.setWindowTitle('Справка')
        self.setWindowIcon(QIcon('resources/54544.png'))
        self.setStyleSheet("background-color: orange;")

        self.label = QLabel()
        self.label.setStyleSheet("font: 12pt Arial; color: black; padding: 10px;")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)

    def add_names(self):
        try:
            films = self.film_service.all_films()
            if films:
                film_info = '\n'.join([f"{film.film_id} - {film.film_name}" for film in films])
            else:
                film_info = "Нет доступных фильмов."
            self.label.setText(film_info)
        except Exception as e:
            self.label.setText("Ошибка при загрузке фильмов.")
            print(e)
