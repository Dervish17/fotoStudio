from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from app.reservWin import AddOrder

class ButtonWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #000000;")
        self.setWindowTitle('Фотостудия "Narcissus"')
        self.resize(300, 400)
        self.setWindowIcon(QIcon('resources/12.png'))

        button_style = """
                                    QPushButton {
                                        font-size: 18px; 
                                        background-color: #ffb8c6; 
                                        color: black; 
                                        border: none; 
                                        padding: 13px; 
                                        border-radius: 5px;
                                    }
                                    QPushButton:hover {
                                        background-color: #f0768b;
                                    }
                                    QPushButton:pressed {
                                        background-color: #ddadaf;
                                    }
                                """
        self.rename_btn = QPushButton('Редактировать записи')
        self.rename_btn.setStyleSheet(button_style)
        self.rename_btn.setFont(QFont('Monotype Corsiva'))
        self.choose_btn = QPushButton('Брони')
        self.choose_btn.setStyleSheet(button_style)
        self.choose_btn.setFont(QFont('Monotype Corsiva'))

        # self.choose_btn.clicked.connect(self.show_choose_note)

        main_l = QVBoxLayout()
        h_l2 = QHBoxLayout()
        h_l3 = QHBoxLayout()

        h_l2.addStretch()
        h_l2.addWidget(self.rename_btn, 2)
        h_l2.addStretch()
        h_l3.addStretch()
        h_l3.addWidget(self.choose_btn, 2)
        h_l3.addStretch()

        main_l.addStretch()
        main_l.addLayout(h_l2)
        main_l.addStretch()
        main_l.addLayout(h_l3)
        main_l.addStretch()

        self.setLayout(main_l)

    # def show_rename_note(self):
    #     self.rename = ()
    #     self.rename.show()
    #
    # def show_choose_note(self):
    #     print('Order')
    #     self.choose = AddOrder()
    #     self.choose.show()

    #
    # def closeEvent(self, event):
    #     QApplication.quit()

