#Успадкування класів
class Grandparent:
    height = 150
    age = 60
    eyes_color = 'Blue'

    def print_values(self):
        print(f'{self} atributes: ')
        print(self.height)
        print(self.eyes_color)
        print(self.age)


class Parent(Grandparent):
    #height = 170
    eyes_color = 'Blue'


class Child(Parent): #Child -> Parent -> Grandparent
    age = 15


class Hello_world:
    hello = 'Hello'
    _hello = '_Hello'
    __hello = '__Hello'
    def __init__(self):
        self.world = 'World'
        self._world = '_World'
        self.__world = '__World'

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hello_world2(Hello_world):
    def printer2(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

    #anna = Grandparent()
#bob = Parent()
#anton = Child()
#anna.print_values()
#bob.print_values()
#anton.print_values()
hw = Hello_world()  #1 слеш - просто захист від підказок, два слеша інкапсоляція даних (захист данних)
#print(hw.hello)
#hw.printer()
hw2 = Hello_world2()
hw2.printer2()

