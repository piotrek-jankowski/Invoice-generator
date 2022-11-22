from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QFileDialog
from Views.screen_ex import Screen


class Invoice_generator:
    def __init__(self, *args, **kwargs):
        self.screen_window = Screen()
        self.screen_window.show()
        
        self.connect_buttons()

        
    def connect_buttons(self):
        self.screen_window.button_template.clicked.connect(self.browse_files)

    def browse_files(self):
        file_name = QFileDialog.getOpenFileName(None, "Open File", ".", "Invoice Template(*_template.docx)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    instance = Invoice_generator()

    sys.exit(app.exec())
