# Написать программу Город.
# Создать три отдельных объекта: City, Street, House.
# У города должны быть улицы (City -> [Street]), у улиц должны быть дома
# Street -> [House].
# У города есть улицы и дома и возможности их добавлять и удалять.
#
#    Улицы могут вместить случайное количество домов от 5 до 20.
#    Дома могут иметь случайное количество населения от 1 до 100.
#    Должна быть возможность наполнить город одним методом.
#    У города должен быть метод который вернет количество населения.
#    *доп. Написать метод который сможет напечатать таблицей:
# Улица Дом Население
#    1   1         5
#    1   2         10
#    1   3         25
#                  и т.д.
import random


class City:
    def __init__(self, name: str):
        self.name = name
        self.streets = []
        self.add_street()

    def add_street(self):
        for name in ['Deribasovskaya', 'Pushkinskaya', 'Evreyskaya',
                     'Kanatnaya']:
            self.streets.append(Street(name))

    def print_table(self):
        print("{:<20} {:<20} {:<15}".format('Street', 'House', 'Residents'))
        for streets_num in range(len(self.streets)):
            for house_num in range(len(self.streets[streets_num].houses)):
                street = self.streets[streets_num].name
                house = self.streets[streets_num].houses[house_num].number
                res = self.streets[streets_num].houses[house_num].residents
                print("{:<20} House # {:<12} {} residents".
                      format(street, house, res))

    def total_residents(self):
        residents = []
        for streets_num in range(len(self.streets)):
            for house_num in range(len(self.streets[streets_num].houses)):
                residents.append(self.streets[streets_num].houses[house_num].
                                 residents)
        print(f'Total residents in city is: {sum(residents)} persons')


class Street:
    def __init__(self, name: str):
        self.name = name
        self.houses = []
        self.add_houses()

    def add_houses(self):
        num = 1
        for amount in range(random.randrange(5, 20)):
            self.houses.append(House(num))
            num += 1


class House:
    def __init__(self, number):
        residents = random.randrange(1, 100)
        self.number = number
        self.residents = residents


odessa = City('Odessa')
odessa.print_table()
odessa.total_residents()

