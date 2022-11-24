from datetime import date
from pathlib import Path
from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QFileDialog


def open_file_template():
    template_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    file_template = QFileDialog.getOpenFileName(None, "Select template file", template_path, "Microsoft Word file (*_template.docx)")
    if file_template:
        file_template_path = Path(file_template[0])
    
    return file_template_path
    
    
def open_file_data():
    data_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    
    file_data = QFileDialog.getOpenFileName(None, "Select data file", data_path, "Data source files (*.xml *.json)")
    if file_data:
        file_data_path = Path(file_data[0])

    return file_data_path
    

def open_file_destination(file_template_path):
    date_today = str(date.today())
    name_hint = ""
    if file_template_path != None and str(file_template_path) != '.':
        name_hint = file_template_path.name.rsplit('_template.docx',1)[0]+"_"
    destination_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)+"\\"+name_hint+"invoice_"+date_today

    file_destination = QFileDialog.getSaveFileName(None, "Save destination file", destination_path, "Microsoft Word file (*.docx)")
    if file_destination:
        file_destination_path = Path(file_destination[0])
    
    return file_destination_path
