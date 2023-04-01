def checker(function, *args, **kwargs):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have a problem: {exc}')
        else:
            print(f'No problems, result: {result}')
    return checker

@checker     #Декоратор
def calculate(expression):
    return eval(expression)

#yield   робить генератор
calculate('2+2')

