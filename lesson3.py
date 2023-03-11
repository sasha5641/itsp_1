class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Hi! im {self.name}'



class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f'Names of {self.brand} passengers: ')
            for element in self.passengers:
                print(element)
        else:
            print(f'There are no passengers in {self.brand}!')


anna = Human(name='Anna')
sergiy = Human(name='Sergiy')

honda = Auto(brand='Honda')
honda.add_passengers(anna)
honda.add_passengers(sergiy)

honda.print_passengers_names()