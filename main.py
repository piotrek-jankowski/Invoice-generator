import sys
from PySide6.QtWidgets import QApplication
from Views.screen_ex import Screen


class Invoice_generator:
    def __init__(self, *args, **kwargs):
        self.screen_window = Screen()
        self.screen_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    instance = Invoice_generator()

    sys.exit(app.exec())
