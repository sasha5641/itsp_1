class Hello:
    def __init__(self):
        print('Hello!')


class World(Hello):
    def __init__(self):
        super().__init__()
        print('World!')

class Class1:
    var = 20

    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

