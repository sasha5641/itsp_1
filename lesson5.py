import tkinter                                  #Інтроспекція
import inspect
import sys
import sqlite3

#sqlite3.connect(database=) #Сама база данних
#sqlite3.enable_callback_tracebacks(True/False) #Увімкнення або вимкнення трасування зворотного дзвінка
#sqlite3.register_adapter    #Реєструє адаптер, який можна викликати, щоб адаптувати тип Python до Тип SQLite
#sqlite3.register_converter('ім'я типу', 'конвертер') #Реєструє конвертер, який можна викликати, щоб перетворити об'єкти SQLite з ім'ям типу в об'єкт Python певного типу
#




def first_func():
    pass


class First_class:
    def printer(self):
        pass

class Second_class(First_class):
    pass

tk = tkinter
first_f = first_func
first_c = First_class

a = 'Hello'
b = 1
c = True
'''
print(tk.__name__)
print(tkinter.__name__)
print(first_func().__name__)
print(first_f.__name__)
print(First_class.__name__)
print(first_c.__name__)
'''
'''
print(type(tkinter))
print(type(a))
print(type(b))
print(type(c))
print(type(first_f))
'''

fc = First_class()

#print(hasattr(a, 'count'))#Чи має функція функцію
#print(getattr(First_class, 'lower', 'МЕТОДУ НЕМАЄ'))#Повертає метоd
#print(callable(first_f))
#print(issubclass(Second_class, First_class))#Перевіряє на залежність klassy
#print(isinstance(fc, First_class))#Перевіряє на залежність functsii

#print(inspect.ismodule(a))#Чи це модуль
#print(inspect.ismethod(First_class))
#print(inspect.isclass(str))#Чи це об'єкт
#print(inspect.getmodule(requests))
#print(sys.version)#Версія пайтону
#print(sys.copyright)#На пайтон

#for key, value in sys.module.items():#Модулі які встановлені
    #print(f'{key} - {value}')

__builtins__