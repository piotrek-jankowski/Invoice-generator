import sys
from PySide6.QtWidgets import QApplication
from Views.screen_ex import Screen
from modules import generate_invoice, file_opener


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
        self.screen_window.button_generate.clicked.connect(self.invoice_generate)

    def activate_button_generate(self):
        if (
                (self.screen_window.label_template_file.text() != '') and 
                (self.screen_window.label_data_file.text() != '') and 
                (self.screen_window.label_destination_file.text() != '')
        ):
            self.screen_window.button_generate.setEnabled(True)
        else:
            self.screen_window.button_generate.setDisabled(True)

    def invoice_generate(self):
        generate_invoice.invoice_generate(self.file_template_path, self.file_data_path, self.file_destination_path)

    def open_file_template(self):
        self.file_template_path = file_opener.open_file_template()
        self.screen_window.label_template_file.setText(self.file_template_path.name)
        self.activate_button_generate()
    
    def open_file_data(self):
        self.file_data_path = file_opener.open_file_data()
        self.screen_window.label_data_file.setText(self.file_data_path.name)
        self.activate_button_generate()

    def open_file_destination(self):
        self.file_destination_path = file_opener.open_file_destination(self.file_template_path)
        self.screen_window.label_destination_file.setText(self.file_destination_path.name)
        self.activate_button_generate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    instance = Invoice_generator()

    sys.exit(app.exec())
