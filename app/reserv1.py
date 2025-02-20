from PyQt6.QtCore import QDateTime
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QTimeEdit, QDateTimeEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QMessageBox

from database import SessionLocal

class AddOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.db = SessionLocal()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.resize(600, 600)
        self.setWindowTitle('Запись на съемку')
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
                    QLineEdit{padding: 5px; font: 12pt Monotype Corsiva; color: white;
                    }
                    QDateTimeEdit{font: 12pt Monotype Corsiva; color: white;
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

        label_session_datetime = QLabel("Укажите дату и время релиза:")
        label_session_datetime.setStyleSheet(style)
        self.session_datetime = QDateTimeEdit(QDateTime.currentDateTime())
        self.session_datetime.setCalendarPopup(True)
        self.session_datetime.setStyleSheet(style)



        self.button_add = QPushButton('Добавить')
        self.button_add.setStyleSheet(style)
        # self.button_add.clicked.connect(self.add_cinema)
        self.button_add.setFont(QFont('Monotype Corsiva'))

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet(style)
        self.button_cancel.clicked.connect(self.add_cancellation)
        self.button_cancel.setFont(QFont('Monotype Corsiva'))

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
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
        main_layout.addWidget(label_session_datetime)
        main_layout.addWidget(self.session_datetime)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    # def add_cinema(self):
    #     film_name = self.text.text()
    #     film_genre = self.genre.currentText()
    #     film_release = self.session_datetime.dateTime().toString("dd.MM.yyyy HH:mm")
    #
    #     if not film_name.strip():
    #         msg_box = QMessageBox()
    #         msg_box.setWindowTitle("Ошибка")
    #         msg_box.setText("Введите имя и фамилию!")
    #         msg_box.setIcon(QMessageBox.Icon.Information)
    #         msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    #         msg_box.setStyleSheet("background-color: white; color: black;")
    #         msg_box.exec()
    #         return
    #
    #     try:
    #         order_service = OrderService(self.db)
    #         films = film_service.get_names_films()
    #         film_names = [film.film_name for film in films]
    #         print(film_names)
    #         film_service.add_film(
    #                              film_name=film_name,
    #                              film_genre=film_genre,
    #                              film_release=str(film_release),
    #                              )
    #         msg_box = QMessageBox()
    #         msg_box.setWindowTitle("заявка на фотосесию добавлен")
    #         msg_box.setText(f"ФИО: {film_name}\n"
    #             f"Жанр фотосъемки: {film_genre}\n"
    #             f"дата фотосъемки: {film_release}\n")
    #         msg_box.setIcon(QMessageBox.Icon.Information)
    #         msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    #         msg_box.setStyleSheet("background-color: white; color: black;")
    #         msg_box.exec()
    #     except ValueError:
    #         msg_box = QMessageBox()
    #         msg_box.setWindowTitle("Ошибка")
    #         msg_box.setText("Введите корректный рейтинг!")
    #         msg_box.setIcon(QMessageBox.Icon.Information)
    #         msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    #         msg_box.setStyleSheet("background-color: white; color: black;")
    #         msg_box.exec()

    def add_cancellation(self):
        self.close()
