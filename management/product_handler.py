from menu import products

"""
Esse módulo ficará responsável por concentrar suas funções de
interação com os produtos do arquivo menu.py que já se encontram
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


def add_product(menu, **kwargs):

    required_attributes = [
        "title", "price", "rating", "description", "type"
    ]
    received_attributes = []

    for key in kwargs.keys():
        received_attributes.append(key)

    required_attributes.sort()
    received_attributes.sort()

    if required_attributes == received_attributes:
        # Organizing list by id:
        def sort_by_id(key):
            return key["_id"]

        menu.sort(key=sort_by_id)
        max_id_number = 1

        if len(menu) > 0:
            for element in menu:
                for key, value in element.items():
                    if key == "_id":
                        if value > max_id_number:
                            max_id_number = value + 1
                            kwargs["_id"] = max_id_number
                            menu.append(kwargs)
        else:
            kwargs["_id"] = len(menu) + 1
            menu.append(kwargs)

        return menu[-1]
    else:
        return "Required attributes: title, price, rating, description, type"
