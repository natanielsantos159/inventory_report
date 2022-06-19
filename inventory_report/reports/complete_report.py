
from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products_list):
        simple_report = SimpleReport.generate(products_list)

        companies_stock_quantity = Counter()
        for product in products_list:
            companies_stock_quantity[product['nome_da_empresa']] += 1

        companies_stock_quantity_str = ''
        for company, quantity in companies_stock_quantity.items():
            companies_stock_quantity_str += f"- {company}: {quantity}\n"

        return (
          f"{simple_report}\n"
          "Produtos estocados por empresa:\n"
          f"{companies_stock_quantity_str}"
        )

