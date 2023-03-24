import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hungry = 50 #Щастя
        self.energy = 2 #Прогрес у навчанні
        self.alive = True #Чи живий студент, чи програв

    def eat(self):
        print('Time to eat!')
        self.energy += 2
        self.hungry -= 2
    def to_sleep(self):
        print('I will sleep!')
        self.energy += 3
        self.hungry += 3
    def to_chill(self):
        print('Rest time')
        self.hungry += 1
        self.energy -= 4
    def is_alive(self):
        if self.energy <= -0.5:
            print('Cast out')
            self.alive = False
        elif self.hungry <= 0:
            print('Non eat')
            self.alive = False
        elif self.energy <= 0:
            print('Passed extrenally')
            self.alive = False

    def end_of_day(self):
        print(f'Hungry = {self.hungry}')
        print(f'Energy = {round(self.energy, 2)}')

    def live(self, day):
        day = f'Day #{day} of {self.name} life!'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.eat()
        elif cube == 2:
            self.to_chill()
        elif cube == 3:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()

alisa = Cat('Alisa')

for day in range(1, 31):
    if alisa.alive:
        alisa.live(day)
    else:
        print('The end!')
        break
else:
    print('Game complete!')