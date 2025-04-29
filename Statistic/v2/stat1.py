# Вам доступен файл students.csv, содержащий данные о студентах учебного курса. 
# В первом столбце записана фамилия, во втором — имя, в третьем — прогресс по курсу в процентах. 
# Напишите программу, которая определяет самое популярное имя и выводит его с заглавной буквы. 
# Если таких имен несколько, программа должна вывести их через запятую в алфавитном порядке, каждое с заглавной буквы.

import csv
import statistics

with open('students.csv', newline='', encoding='utf8') as file:
    res = csv.reader(file)

    names = []

    for row in res:
        names.append(row[1].capitalize())
    
    modes = statistics.multimode(names)

    print(*sorted(modes))