import random


class Programmer:
    def __init__(self, name='Programmer', language=None):
        self.name = name
        self.language = language
        self.gladness = 25
        self.knowledge = 0
        self.money = 50
        self.satiety = 50

    def eat(self):
        if self.satiety > 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.money -= 25

    def chill(self):
        self.gladness += 10

    def code(self):
        self.knowledge += 10
        self.gladness -= 8
        self.money += 25
        return f"{self.name} is coding in {self.language}"

    def attend_meeting(self, meeting):
        self.knowledge += 10
        self.gladness -= 6
        return f"{self.name} is attending a meeting about {meeting.topic}"

    def days_indexes(self, day):
        day = f'Today the {day} of {self.name} life!'
        print(f'{day:=^50}')

        print('Human`s indexes:')
        print(f'Money - {self.money}')
        print(f'Gladness - {self.gladness}')
        print(f'Satiety - {self.satiety}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.knowledge < 0:
            print('Fired...')
            return False
        if self.money <= 0:
            print('Bankrupt...')
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if not self.language:
            print("Choose a language to code in")
            return

        self.days_indexes(day)

        if self.satiety < 20:
            print('EAT!')
            self.eat()

        elif self.gladness < 20:
            print('Let`s chill!')
            self.chill()

        else:
            dice = random.randint(1, 4)

            if dice == 1:
                print('Code')
                print(self.code())

            elif dice == 2:
                print('Meeting')
                meeting = Meeting("New project")
                print(self.attend_meeting(meeting))

            elif dice == 3:
                print('Chill')
                self.chill()

            else:
                print('Eat')
                self.eat()


class Meeting:
    def __init__(self, topic):
        self.topic = topic


programmer = Programmer(name='Alice', language='Python')

for day in range(1,30):
    if programmer.live(day) == False:
        print('Game over')
        break