from functools import partial
import sys
from pathlib import Path
from datetime import date
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import QStandardPaths
from Views.screen_ex import Screen


class Invoice_generator:
    def __init__(self, *args, **kwargs):
        self.file_template_path = None
        self.file_data_path = None
        self.file_destination_path = None

        self.screen_window = Screen()
        self.screen_window.show()
        
        self.connect_buttons()

        
    def connect_buttons(self):
        self.screen_window.button_template.clicked.connect(self.open_file_template)
        self.screen_window.button_data.clicked.connect(self.open_file_data)
        self.screen_window.button_destination.clicked.connect(self.open_file_destination)

    def open_file_template(self):
        template_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        
        file_template = QFileDialog.getOpenFileName(None, "Select template file", template_path, "Microsoft Word file (*_template.docx)")
        if file_template:
            self.file_template_path = Path(file_template[0])
            self.screen_window.label_template_file.setText(self.file_template_path.name)
        
        self.activate_button_generate()
    def open_file_data(self):
        data_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        
        file_data = QFileDialog.getOpenFileName(None, "Select data file", data_path, "Data source files (*.xml *.json)")
        if file_data:
            self.file_data_path = Path(file_data[0])
            self.screen_window.label_data_file.setText(self.file_data_path.name)
        
        self.activate_button_generate()
    def open_file_destination(self):
        date_today = str(date.today())
        name_hint = ""
        if self.file_template_path is not None:
            name_hint = self.file_template_path.name.rsplit('_template.docx',1)[0]+"_"
        destination_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)+"\\"+name_hint+"invoice_"+date_today

        file_destination = QFileDialog.getSaveFileName(None, "Save destination file", destination_path, "Microsoft Word file (*.docx)")
        if file_destination:
            self.file_destination_path = Path(file_destination[0])
            self.screen_window.label_destination_file.setText(self.file_destination_path.name)
        
        self.activate_button_generate()

    def activate_button_generate(self):
        if (
                (self.screen_window.label_template_file.text() != '') and 
                (self.screen_window.label_data_file.text() != '') and 
                (self.screen_window.label_destination_file.text() != '')
        ):
            self.screen_window.button_generate.setEnabled(True)
        else:
            self.screen_window.button_generate.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    instance = Invoice_generator()

    sys.exit(app.exec())
