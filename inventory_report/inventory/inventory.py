import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",")
            data = list(file_reader)

        if report_type == "simples":
            result_report = SimpleReport.generate(data)
        elif report_type == "completo":
            result_report = CompleteReport.generate(data)

        return result_report
