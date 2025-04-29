# Вам доступен файл data.csv, который содержит данные о жителях России, работающих в государственных образовательных учреждениях. В первых трех столбцах записано ФИО, в четвертом — регион проживания, в пятом — текущая заработная плата в рублях. Напишите программу, которая определяет следующие характеристики:

# - средняя заработная плата
# - медианная заработная плата
# - размах выборки (разница между максимальной и минимальной заработной платой)

import csv
import statistics

with open('data.csv', newline='', encoding='utf8') as file:
    res = csv.reader(file)

    salaries = []

    for row in res:
        if row[4].isdigit():
            salaries.append(int(row[4]))
      
    average = statistics.mean(salaries)
    median = statistics.median(salaries)
    swing = max(salaries) - min(salaries)

print(f'Средняя заработная плата = {round(average)}')
print(f'Медианная заработная плата = {round(median)}')
print(f'Размах выборки = {swing}')