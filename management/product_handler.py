from menu import products

"""
Esse módulo ficará responsável por concentrar suas funções de 
interação com os produtos do arquivo menu.py que já se encontra 
na raiz do projeto.
"""


def get_product_by_id(id):

    product = {}

    for element in products:
        for key, value in element.items():
            if key == "_id" and value == id:
                product = element
                break

    return product


def get_products_by_type(product_type):

    list = []

    for item in products:
        if item.get("type") == product_type:
            list.append(item)

    return list
