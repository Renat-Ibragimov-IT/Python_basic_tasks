# Написать программу кофейный магазин.
# Обьекты:
#    Product
#    - свойства: наименование, тип, цена
#    - print обьекта продукта должен возвращать прим. "Кофе: Эспрессо, цена:
#    27грн."
#    Store
#    - может импортировать продукты из файла invertory.csv
#    (по-умолчанию по 5 шт. каждого наименования)
#    - может вернуть список продуктов нужного типа
#    (tea, coffee или все продукты)
#    - может вернуть общую стоимость продуктов в наличии
#    - может продать продукт
# *доп. Научить Store запоминать выручку(сумма проданных продуктов)
# и выводить баланс.
# Тип продукта может быть только coffee или tea
# (нельзя создать обьект с другим типом).
import csv


class Product:

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
    def __init__(self):
        self.products = []
        self.income = 0
        self.inventory()

    def inventory(self):
        with open('inventory.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'tea' or row['Type'] == 'coffee':
                    self.products.extend(([Product(row['Name'], row['Type'],
                                                          float(row['Price']))
                                                          for _ in range(5)]))

    def initial_overall_coast(self):
        return sum(item.price for item in self.products)

    def sell_a_product(self, product: str):
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

