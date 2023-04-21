from menu import products

"""
Esse módulo ficará responsável por concentrar suas funções de
interação com os produtos do arquivo menu.py que já se encontram
na raiz do projeto.
"""


def get_product_by_id(_id):
    # try:
    #     if type(_id) != "int":
    #         raise TypeError()
    # except TypeError:
    #     return "product id must be an int"

    product_dict = {}
    for product in products:
        if product["_id"] == _id:
            product_dict.update(product)

    return product_dict


def get_products_by_type(product_type):
    # try:
    #     if type(product_type) != "str":
    #         raise TypeError()
    # except TypeError:
    #     return "product id must be an str"

    list = []
    for product in products:
        if product.get("type") == product_type:
            list.append(product)

    return list


def add_product(menu, **kwargs):
    required_attributes = ["title", "price", "rating", "description", "type"]
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

                            # Creating a new key in the received kwargs:
                            kwargs["_id"] = max_id_number
                            menu.append(kwargs)
        else:
            kwargs["_id"] = len(menu) + 1
            menu.append(kwargs)

        return menu[-1]
    else:
        return "Required attributes: title, price, rating, description, type"


def menu_report():
    product_count = len(products)
    average_price = 0
    most_common_type = None

    product_types = []
    sum_of_values = 0
    for product in products:
        product_types.append(product["type"])
        sum_of_values += product["price"]
        average_price = sum_of_values / product_count

    type_count = []
    for _type in set(product_types):
        count = product_types.count(_type)
        type_count.append({_type: count})

    max_number = 0
    for _type in type_count:
        for key, value in _type.items():
            if value > max_number:
                max_number = value
                if max_number == value:
                    most_common_type = key

    return f"Product Count: {product_count} - Average Price: {round(average_price, 2)} - Most Common Type: {most_common_type}"


def add_product_extra(menu, **kwargs):
    ...
