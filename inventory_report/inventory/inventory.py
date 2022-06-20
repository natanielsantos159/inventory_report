import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict


class Inventory:
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            file_extension = path.split('.')[-1]
            read_by_extension = {
                "csv": Inventory.read_csv,
                "json": Inventory.read_json,
                "xml": Inventory.read_xml
            }

            data = read_by_extension.get(file_extension)(file)

        if report_type == "simples":
            result_report = SimpleReport.generate(data)
        elif report_type == "completo":
            result_report = CompleteReport.generate(data)

        return result_report

    def read_csv(file):
        file_reader = csv.DictReader(file, delimiter=",")
        return list(file_reader)

    def read_json(file):
        return json.load(file)

    def read_xml(file):
        xml_string = file.read()
        return xmltodict.parse(xml_string)['dataset']['record']
