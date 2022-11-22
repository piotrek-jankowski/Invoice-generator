from Views import screen
from PySide6.QtWidgets import QWidget

class Screen(QWidget, screen.Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Invoice generator")
