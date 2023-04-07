import random

class MathOperation:
    def __init__(self, *args):
        self.numbers = args
        self.result = None

    def __repr__(self):
        if self.result is None:
            self.calculate()
        return str(self.result)

    def calculate(self):
        operation = random.choice(['+', '-', '*', '/'])
        result = self.numbers[0]
        for number in self.numbers[1:]:
            if operation == '+':
                result += number
            elif operation == '-':
                result -= number
            elif operation == '*':
                result *= number
            elif operation == '/':
                result /= number
        self.result = result

math_operation = MathOperation(4, 9, 2)
print(math_operation)