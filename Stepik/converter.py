a = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16}

while True:
    s = input('В какую систему переводить?\n2 - двоичная\n8 - восьмеричная\n10 - десятичная\n16 - шестнадцатиричная\n')
    if s in ['2', '8', '10', '16']:
        break
    else:
        print('Неверный ввод!\nВведите 2, 8, 10 или 16\n')

if s != '10':
    while True:
        try:
            num = int(input('Введите число в десятичной системе\n'))
        except (TypeError, ValueError):
            print('Введите число. Иные символы не допустимы\n')
        else:
            break

else:
    ss = int(input('Из какой системы переводить?\n2 - двоичной\n8 - восьмеричной\n16 - шестнадцатиричной\n'))
    while True:
        num = list(input(f'Введите число в {ss}-ичной системе\n'))
        if (ss == 2 and len(set(num).difference({'0', '1'})) == 0) \
        or (ss == 8 and len(set(num).difference({'1', '2', '3', '4', '5', '6', '7', '8'})) == 0) \
        or (ss == 16 and len(set(num).difference({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G' \
        'a', 'b', 'c', 'd', 'e', 'f', 'g'})) == 0):
            break

        else:
            print('Неверная система счисления. Повторите ввод')


def dec(num):
    n10 = 0
    for i in range(len(num)):
        if num[i].upper() in a:
            num[i] = str(a[num[i].upper()])
        
    for i in range(len(num)):
        n10 += int(num[i]) * ss ** (len(num) - 1 - i)
    return n10

c = {'2': bin, '8': oct, '16': hex, '10': dec}

print(str(c[s](num)).lstrip('0').lstrip('x').lstrip('b').lstrip('o'))

