print('Конвертація з метричної в неметричну')
convertation = int(input('Що рахуємо: \n 1. Температура\n 2. Вага\n 3. Довжина\n 4. Об\'єм\n 5. Швидкість\n '))

if convertation == 1:
    temperature = int(input(' 1. Цельсій -> Фаренгейт\n 2. Цельсій -> Кельвін\n'))
    if temperature == 1:
        value_temperature = float(input('Скільки градусів за Цельсієм? :\n'))
        print(value_temperature, 'градусів за Цельсієм становлять', round((((9 / 5) * value_temperature + 32)), 2), \
                'градусів за Фаренгейтом')
    elif temperature == 2:
        value_temperature = float(input('Скільки градусів за Цельсієм? :\n'))
        print(value_temperature, 'градусів за Цельсієм становлять', round((value_temperature + 273.15), 2), \
                'градусів за Кельвіном')

elif convertation == 2:
    massa = int(input(' 1. Кілограми -> фунти\n 2. Грами -> унції \n'))
    if massa == 1:
        value_massa = float(input('Скільки кілограм? :\n'))
        print(value_massa, 'кілограм становлять', round((value_massa * 2.20462), 2), 'фунтів')
    elif massa == 2:
        value_massa = float(input('Скільки грам? :\n'))
        print(value_massa, 'грам становлять', round((value_massa * 0.035274), 2), 'унцій')

elif convertation == 3:
    dlina = int(input(' 1. Кілометри -> милі\n 2. Метри -> ярди\n 3. Метри -> фути\n 4. Сантиметри -> дюйми\
    \n 5. Мілліметри -> дюйми \n'))
    if dlina == 1:
        value_dlina = float(input('Скільки кілометрів? :\n'))
        print(value_dlina, 'кілометрів становлять', round((value_dlina * 1.60934), 2), 'мил')
    elif dlina == 2:
        value_dlina = float(input('Скільки метрів? :\n'))
        print(value_dlina, 'метрів становлять', round((value_dlina * 1.09361), 2), 'ярд')
    elif dlina == 3:
        value_dlina = float(input('Скільки метрів? :\n'))
        print('Конвертація з метричної в неметричну')
        convertation = int(input('Що рахуємо: \n 1. Температура\n 2. Вага\n 3. Довжина\n 4. Об\'єм\n 5. Швидкість\n '))
elif convertation == 4:
    space = int(input(' 1. Літри -> галони\n 2. Літри -> пінти\n'))
    if space == 1:
        value_space = float(input('Скільки літрів? : '))
        print(value_space,'літрів становить', round((value_space / 3.785411784), 2), 'галонів')
    elif space == 2:
        value_space = float(input('Скільки літрів? :\n'))
        print(value_space, 'літрів становить', round((value_space / 0.56826125), 2), 'пінти')
elif convertation == 5:
    speed = float(input(' Скільки кілометрів за годину? : '))
    print(speed, 'кілометрів за годину становить ', round((speed / 1.60934), 2), 'милей за годину')
