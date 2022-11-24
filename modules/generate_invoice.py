import json, xmltodict
from docxtpl import DocxTemplate
from pathlib import Path


def invoice_generate(template_file_path, data_file_path, destination_file_path):
    def open_data_file():
        
        def postprocessor(path, key, value):  # convert "None" to ''
            if not value:
                return key, ''
            return key, value
        
        if data_file_path.suffix.lower() == ".json":
            with open(data_file_path, encoding="utf-8") as fl:
                data = json.load(fl)
            return data
        elif data_file_path.suffix.lower() == ".xml":
            file = open(data_file_path, "r", encoding="utf-8")
            data = xmltodict.parse(file.read(), postprocessor = postprocessor)["root"]
            return data
        

    tpl = DocxTemplate(template_file_path)
    tpl.render(open_data_file())
    tpl.save(destination_file_path)
    return 0