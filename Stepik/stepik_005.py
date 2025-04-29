data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

#new_data = sorted(list(map(lambda x: x[::-1], data)), key=lambda y: y[0][-1])

#new_data = list(map(lambda x: x[0] + ': ' + str(x[1]), new_data))


#new_data = list(map(lambda x: x[0] + ': ' + str(x[1]), sorted(list(map(lambda x: x[::-1], data)), key=lambda y: y[0][-1])))

#print(*list(map(lambda x: x[0] + ': ' + str(x[1]), sorted(list(map(lambda x: x[::-1], data)), key=lambda y: y[0][-1], reverse=True))), sep='\n')

for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
    print(f'{city}: {pop}')