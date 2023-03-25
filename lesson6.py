#Обробник виключень
def sum_numbers(num1, num2, num3):
    num1 = int(num1)  #int ctili chisla
    num2 = int(num2)
    num3 = int(num3)

    res = num1 + num2 + num3
    return res


n_1 = input('Введіть число 1: ')
n_2 = input('Введіть число 2: ')
n_3 = input('Введіть число 3: ')
print(sum_numbers(n_1, n_2, n_3))
