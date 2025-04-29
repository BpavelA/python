direction = input('Выберите направление конвертации:\n db = 10 -> 2, do = 10 -> 8, dx = 10 -> 16,\n bd = 2 -> 10, od = 8 -> 10, xd = 16 -> 10\n')

def decN(nn):
    n10 = 0
    
    if s[direction][1] == 16:
        a = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16}
        nn = list(str(nn))
        for i in range(len(nn)):
            if nn[i].upper() in a:
                nn[i] = a[i]
        nn = ''.join(nn)
    
    for i in range(len(str(nn))):
        n10 += int(str(nn)[i]) * s[direction][1] ** (len(str(nn)) - 1 - i)
    
    return n10

s = {'db': [bin], 'do': [oct], 'dx': [hex], 'bd': [decN, 2], 'od': [decN, 8], 'xd': [decN, 16]}

print(str(s[direction][0](int(input('Введите число: ')))).lstrip('0').lstrip('x').lstrip('b').lstrip('o'))

