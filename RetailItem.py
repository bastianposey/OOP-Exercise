import RetailItemClass as rc

#creating objects
item_1 = rc.Retail("Jacket", 12, 59.95)
item_2 = rc.Retail("Designer Jeans", 40, 34.95)
item_3 = rc.Retail("Shirt", 20, 24.95)

#printing out item objects
print(item_1.get_description(),item_1.get_units(),item_1.get_price())
print(item_2.get_description(),item_2.get_units(),item_2.get_price())
print(item_3.get_description(),item_3.get_units(),item_3.get_price())