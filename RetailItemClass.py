class Retail:
    
# initializing retail class
    def __init__(self, des, unit, price):
        self.__description = des
        self.__units = unit
        self.__price = price

# returns the description
    def get_description(self):
        return self.__description
# returns the units

    def get_units(self):
        return self.__units

# returns the price 
    def get_price(self):
        return self.__price