# На вход программе подаётся одна строка – сгенерированный ИИ автомобильный номер.
# Формат номера
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>

number = input()

if len(number[7:]) in (2, 3) and (number[0] in 'АВЕКМНОРСТУХ') and number[1:4].isdigit() and (number[4] in 'АВЕКМНОРСТУХ') and (number[5] in 'АВЕКМНОРСТУХ') and (number[6] == '_') and number[7:].isdigit():
    print('YES')
else:
    print('NO')