from inventory_report.inventory.product import Product


def test_cria_produto():
    product_info = {
        "id": 1,
        "nome_do_produto": "Caneca",
        "nome_da_empresa": "Trybe",
        "data_de_fabricacao": "12-01-2022",
        "data_de_validade": "12-01-2099",
        "numero_de_serie": 1234567,
        "instrucoes_de_armazenamento": "instrucao de armazenamento",
    }

    caneca = Product(
        product_info["id"],
        product_info["nome_do_produto"],
        product_info["nome_da_empresa"],
        product_info["data_de_fabricacao"],
        product_info["data_de_validade"],
        product_info["numero_de_serie"],
        product_info["instrucoes_de_armazenamento"],
    )

    for key, value in product_info.items():
        assert key in caneca.__dict__.keys()
        assert caneca.__dict__[key] == value
