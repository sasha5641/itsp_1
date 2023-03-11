import random


class Human:
    def __init__(self, name='Human',
                 job=None,
                 home=None,
                 car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.gladness = 50
        self.satiety = 50
        self.money = 100

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if not self.car.drive():
            self.to_repair()
            return
        self.job = Job(jobs)

    def eat(self):
        if self.home.food <= 0:
            self.get_shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel <= 20:
                self.get_shopping('fuel')
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def get_shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel <= 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel!')
            self.money -= 100
            self.car.fuel = 100
        elif manage == 'food':
            print('I bought food!')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Hooray! Delicacies!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 200

    def days_indexes(self, day):
        day = f'Today the {day} of {self.name} life!'
        print(f'{day:=^50}')

        print('Human`s indexes:')
        print(f'Money - {self.money}')
        print(f'Gladness - {self.gladness}')
        print(f'Satiety - {self.satiety}')

        print('Car indexes:')
        print(f'Fuel - {self.car.fuel}')
        print(f'Gladness - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money <= -400:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()

        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('EAT!')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I want to chill, but there is so much mess...')
                self.clean_house()
            else:
                print('Let`s chill!')
                self.chill()
        elif self.money < 0:
            print('Let`s work!')
            self.work()

        if dice == 1:
            print('Let`s work!')
            self.work()
        elif dice == 2:
            print('Let`s chill!')
            self.chill()
        elif dice == 3:
            self.clean_house()
        else:
            self.get_shopping('delicacies')


class Auto:
    def __init__(self, brand_dict):
        self.brand = random.choice(list(brand_dict))
        self.fuel = brand_dict[self.brand]['fuel']
        self.strength = brand_dict[self.brand]['strength']
        self.consumption = brand_dict[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True #Авто поїхало
        else:
            print('Car cannot move!!!')
            return False #Авто не поїхало


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_dict):
        self.job = random.choice(list(job_dict))
        self.salary = job_dict[self.job]['salary']
        self.gladness_less = job_dict[self.job]['gladness_less']


jobs = {
    'Waiter':{
        'salary': 25,
        'gladness_less': 13
    },
    'Python developer': {
        'salary': 50,
        'gladness_less': 7
    },
    'C++ developer': {
        'salary': 60,
        'gladness_less': 10
    },
    'Cleaner': {
        'salary': 10,
        'gladness_less': 20
    },
}

brands_of_car = {
    'BMW': {
        'fuel': 100,
        'strength': 60,
        'consumption': 15
    },
    'Audi': {
        'fuel': 90,
        'strength': 75,
        'consumption': 11
    },
    'Deo': {
        'fuel': 100,
        'strength': 50,
        'consumption': 7
    },
    'Moskvich': {
        'fuel': 100,
        'strength': 10,
        'consumption': 20
    }
}

nick = Human(name='Nick')

for day in range(1,366):
    if nick.live(day) == False:
        print('Game over')
        break
