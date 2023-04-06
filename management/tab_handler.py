from menu import products


def calculate_tab(list_of_dictionaries):

    item_subtotal_list = []
    result = {}

    for dictionary in list_of_dictionaries:
        if "amount" not in dictionary and "id" not in dictionary:
            return "Required attributes: _id, amount"

    for product in products:
        for dictionary in list_of_dictionaries:
            # Finding products by id:
            if dictionary["_id"] == product["_id"]:
                item_subtotal = product["price"] * dictionary["amount"]
                item_subtotal_list.append(item_subtotal)

            subtotal = 0

            for price in item_subtotal_list:
                subtotal += price
                result = {"subtotal": "{:.2f}".format(subtotal)}
    return result
