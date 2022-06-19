import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                file_reader = csv.DictReader(file, delimiter=",")
                data = list(file_reader)
            elif path.endswith(".json"):
                data = json.load(file)

        if report_type == "simples":
            result_report = SimpleReport.generate(data)
        elif report_type == "completo":
            result_report = CompleteReport.generate(data)

        return result_report
