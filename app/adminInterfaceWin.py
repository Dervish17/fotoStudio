from turtledemo.chaos import coosys

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QTableWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QHeaderView, \
    QMessageBox
from database import SessionLocal
from services.order_services import OrderService
from app.adminOrderWin import AddAdminOrder


class Communicate(QObject):
    update_signal = pyqtSignal()


class AdminInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show_orders()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Администратор фотостудии "Narcissus" ')
        self.setStyleSheet("background-color: #000000;")
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
                                QLineEdit{border: 1px solid white; padding: 5px; font: 12pt Monotype Corsiva; color: white;
                                }
                                QDateTimeEdit{font: 12pt Monotype Corsiva; color: white;}
                                QComboBox{font: 12pt Monotype Corsiva; color: white;
                                }
                                        """

        self.table = QTableWidget()
        self.table.setStyleSheet("""
                            QTableWidget {
                                background-color: black;
                                font: 15pt Monotype Corsiva;  
                                color: white; 
                                 
                                border: 1px solid black; 
                            }
                            QHeaderView::section {
                                background-color: #ffb8c6; 
                                font: 12pt Monotype Corsiva;
                                color: black; 
                                font-weight: bold;
                                
                                border: 1px solid #b0b0b0;
                            }
                            QTableWidget::item:selected {
                                background-color: #ffb8c6;
                                color: #000000;
                            }
                            """)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        self.button_delete = QPushButton('Удалить запись')
        self.button_delete.setStyleSheet(style)
        self.button_delete.clicked.connect(self.delete_order)

        self.button_change = QPushButton('Изменить Запись')
        self.button_change.setStyleSheet(style)
        self.button_change.clicked.connect(self.change_order)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_delete)
        layout_buttons.addWidget(self.button_change)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addLayout(layout_buttons)

        self.communicate = Communicate()
        self.communicate.update_signal.connect(self.show_orders)
        self.setLayout(main_layout)

    def show_orders(self):
        db = SessionLocal()
        order_session = OrderService(db)

        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ['Номер записи', 'Имя Фамилия клиента', 'Фотограф', 'Комната', 'Дата', 'Статус'])

        orders = order_session.all_orders()

        self.table.setRowCount(len(orders))
        for row_idx, order in enumerate(orders):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(order.order_id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(order.client_name + " " + order.client_surname)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(order.employee_name)))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(order.room_name)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(order.order_date)))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(order.order_status)))
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

    def delete_order(self):
        if self.table.selectedItems():
            selected_row = self.table.currentRow()
            order_id = int(self.table.item(selected_row, 0).text())

            confirmation_dialog = QMessageBox()
            confirmation_dialog.setStyleSheet("background-color: white; color: black;")
            confirmation_dialog.setWindowTitle("Подтверждение удаления")
            confirmation_dialog.setText(f"Вы уверены, что хотите удалить запись?\n"
                                        f"ID записи: {order_id}")
            confirmation_dialog.setIcon(QMessageBox.Icon.Warning)
            confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirmation_dialog.setDefaultButton(QMessageBox.StandardButton.No)
            user_response = confirmation_dialog.exec()

            if user_response == QMessageBox.StandardButton.Yes:
                db = SessionLocal()
                order_service = OrderService(db)
                order_service.delete_order(order_id)

                self.table.removeRow(selected_row)
                QMessageBox.information(self, "Успешно!", "Запись успешно удална.")

        else:
            QMessageBox.critical(self, "Ошибка", "Запись не выбрана")

    def on_table_row_selected(self):
        row = self.table.currentRow()
        data = []
        if row != -1:
            data.append(self.table.item(row, 0).text())
            data.append(self.table.item(row, 1).text())
            data.append(self.table.item(row, 2).text())
            data.append(self.table.item(row, 3).text())
            data.append(self.table.item(row, 4).text())
            data.append(self.table.item(row, 5).text())
        return data

    def change_order(self):
        self.change = AddAdminOrder(self.on_table_row_selected(), communicate=self.communicate)
        self.change.show()
