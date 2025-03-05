# Item class to support Customer class in making purchases

class Item:
    def __init__(self, item, cost = 0, quantity = 0):
        self.__item = item
        self.__cost = cost
        self.__quantity = quantity

#   Method to calculate the total cost of item object via cost x quantity.
    def calculate_total_cost(self):
        total_cost = self.__cost * self.__quantity
        return total_cost


#   SETTER
    def set_item_name(self, item):
        if isinstance(item, str):
            self.__item = item
        else:
            raise ValueError("Item name must be entered in string format.")

    def set_item_cost(self, cost):
        if isinstance(cost, (int, float)):
            self.__cost = cost
        else:
            raise ValueError("Cost of Item must be a float or integer value.")

    def set_item_quantity(self, quantity):
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ValueError("Quantity must be an integer value.")


#   GETTER
    def get_item_name(self):
        return self.__item

    def get_item_cost(self):
        return self.__cost

    def get_item_quantity(self):
        return self.__quantity