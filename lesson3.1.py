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
        pass

    def work(self):
        pass

    def get_shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_house(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


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
