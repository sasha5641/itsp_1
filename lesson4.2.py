class Monitor:
    def __init__(self):
        super().__init__()
        self.resolution = '4K'

    def dispay(self):
        print('My display 4K')

class Processor:
    def __init__(self):
        super().__init__()
        self.cores = 8

    def calculate(self):
        print('I have 8 cores')

class Computer(Monitor, Processor):
    def info(self):
        print(self.resolution)
        print(self.cores)


asus = Computer()
asus.info()