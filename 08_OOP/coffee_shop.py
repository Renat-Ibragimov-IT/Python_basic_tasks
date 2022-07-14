# Write a program "Coffee shop".
# Objects:
#   Product
#   - properties: name, type, price
#   - print of the product object should return "Coffee: Espresso, price:
#   27UAH."
#   Store
#   - can import products from the inventory.csv file
#   (by default, 5 items of each item)
#   - can return a list of products of the desired type
#   (tea, coffee or all products)
#   - can return the total cost of products in stock
#   - can sell the product
import csv


class Product:
    """This class describes the properties of the "Product" object"""
    def __init__(self, name: str, prod_type: str, price: float):
        if prod_type.lower() not in ['coffee', 'tea']:
            raise ValueError('Sorry')
        self.name = name
        self.prod_type = prod_type
        self.price = price

    def __str__(self):
        return f'{self.prod_type}: {self.name} - Price: ' \
               f'{self.price} UAH'

    def __repr__(self):
        return self.__str__()


class Store:
    """This class describes the properties of the "Store" object"""
    def __init__(self):
        self.products = []
        self.income = 0
        self.inventory()

    def inventory(self):
        """"""
        with open('inventory.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'tea' or row['Type'] == 'coffee':
                    self.products.extend(([Product(row['Name'], row['Type'],
                                                   float(row['Price']))
                                           for _ in range(5)]))

    def initial_overall_coast(self):
        """This function will calculate the initial overall price for
        all products"""
        return sum(item.price for item in self.products)

    def sell_a_product(self, product: str):
        """This function will calculate ov"""
        for index, item in enumerate(self.products):
            if product.lower() == item.name.lower():
                self.products.pop(index)
                self.income += item.price
                break
        return f'Total income: {self.income} UAH'


my_drink = Product('Espresso', 'coffee', 27)
my_shop = Store()
print(my_drink)
print(my_shop.products)
print([item for item in my_shop.products if item.prod_type == 'tea'])
print(my_shop.initial_overall_coast())
print(my_shop.sell_a_product('espresso'))
print(my_shop.sell_a_product('doppio'))
