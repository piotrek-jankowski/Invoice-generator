from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import QStandardPaths
from Views.screen_ex import Screen


class Invoice_generator:
    def __init__(self, *args, **kwargs):
        self.screen_window = Screen()
        self.screen_window.show()
        
        self.connect_buttons()

        
    def connect_buttons(self):
        self.screen_window.button_template.clicked.connect(self.open_file_template)
        self.screen_window.button_invoice.clicked.connect(self.open_file_data)
        self.screen_window.button_destination.clicked.connect(self.open_file_destination)

    def open_file_template(self):
        self.file_template = QFileDialog.getOpenFileName(None, "Select template file", QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation), "Microsoft Word file (*_template.docx)")
    def open_file_data(self):
        self.file_data = QFileDialog.getOpenFileName(None, "Select data file", QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation), "Data source files (*.xml *.json)")
    def open_file_destination(self):
        self.file_destination = QFileDialog.getSaveFileName(None, "Save destination file", QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation), "Microsoft Word file (*.docx)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    instance = Invoice_generator()

    sys.exit(app.exec())
