class MyExcepsion(Exception):
    def __str__(self):
        return 'Hello! It`s my exception!'


#Обробник виключень
    #def sum_numbers(num1, num2, num3):
        #try:
            #num1 = int(num1)  #int ctili chisla
            #num2 = int(num2)            #можна флоат
           # num3 = int(num3)

           # res = num1 / num2 / num3
           # print(res)
        #except ValueError:   #Спрацьовує, якщо блок try вибиває помилку + rkscho  валює ерор воно на 1 помилку валює ерор
            #print('Ви ввели не число!')
        #except ZeroDivisionError:   #Спрацьовує, якщо блок try вибиває помилку + на нуль ділити не можна (ошибка 1 )
           # print('Ділити на 0 не можна!')
       # except Exception:    #Обичний ексцепт на все работает + exception toge takoe ge
           # print('Pomilka')
       # except Exception as exc:
            #print(exc)
        #else:
           # print('Виконано без помилок!')
        #finally:
            #print('Кінець програми!')
def sum_numbers(num1, num2, num3):
    if not num1.isdigit() or not num2.isdigit() or not num3.isdigit():
        raise MyExcepsion #Викликає спеціально помилку

n_1 = input('Введіть число 1: ')
n_2 = input('Введіть число 2: ')
n_3 = input('Введіть число 3: ')
sum_numbers(n_1, n_2, n_3)
