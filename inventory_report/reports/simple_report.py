from datetime import date


class SimpleReport():

    def generate(product_list):
        oldest_product = min(
            product_list,
            key=lambda x: x['data_de_fabricacao'],
        )

        today = date.today().strftime("%d/%m/%Y")
        not_expired_products = filter(
            lambda x: x['data_de_validade'] > today,
            product_list
        )
        closest_expiration_date = min(
            not_expired_products,
            key=lambda x: x['data_de_validade']
        )

        companies_products_quantity = [
            product['nome_da_empresa']
            for product in product_list
        ]

        company_bigger_stock = max(
            set(companies_products_quantity),
            key=companies_products_quantity.count)

        return(
            f"Data de fabricação mais antiga: "
            f"{oldest_product['data_de_fabricacao']}\n"
            f"Data de validade mais próxima: "
            f"{closest_expiration_date['data_de_validade']}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
