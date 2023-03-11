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
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

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
