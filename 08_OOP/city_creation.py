# Write a program "City".
# Create three separate objects: City, Street, House.
# City must have streets (City -> [Street]), streets must have houses
# Street -> [House].
# The city has streets and houses and the ability to add and remove them.
# Streets can fit a random number of houses from 5 to 20.
# Houses can have a random population from 1 to 100.
# It should be possible to fill the city with one method.
# The city must have a method that will return the population.
# *Optional: write a method that can print a table:
# Street House Residents
#    1     1       5
#    1     2       10
#    1     3       25
import random


class City:
    """This class will describe "City" object"""
    def __init__(self, name: str):
        self.name = name
        self.streets = []
        self.add_street()

    def add_street(self):
        """This function will add the streets by names to the city"""
        for name in ['Deribasovskaya', 'Pushkinskaya', 'Evreyskaya',
                     'Kanatnaya']:
            self.streets.append(Street(name))

    def print_table(self):
        """This function will print the table with requested info"""
        print("{:<20} {:<20} {:<15}".format('Street', 'House', 'Residents'))
        for streets_num in range(len(self.streets)):
            for house_num in range(len(self.streets[streets_num].houses)):
                street = self.streets[streets_num].name
                house = self.streets[streets_num].houses[house_num].number
                res = self.streets[streets_num].houses[house_num].residents
                print("{:<20} House # {:<12} {} residents".
                      format(street, house, res))

    def total_residents(self):
        """This function will calculate total residents amount"""
        residents = []
        for streets_num in range(len(self.streets)):
            for house_num in range(len(self.streets[streets_num].houses)):
                residents.append(self.streets[streets_num].houses[house_num].
                                 residents)
        print(f'Total residents in city is: {sum(residents)} persons')


class Street:
    """This class will describe "Street" object"""
    def __init__(self, name: str):
        self.name = name
        self.houses = []
        self.add_houses()

    def add_houses(self):
        """This function will add houses to the street"""
        num = 1
        for amount in range(random.randrange(5, 20)):
            self.houses.append(House(num))
            num += 1


class House:
    """This class will describe "House" object"""
    def __init__(self, number):
        residents = random.randrange(1, 100)
        self.number = number
        self.residents = residents


odessa = City('Odessa')
odessa.print_table()
odessa.total_residents()
