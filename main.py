from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWindow
import sys
import traceback


def main():
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook

if __name__ == '__main__':
    main()