import csv
import statistics

with open('Python/Statistic/students.csv', newline='', encoding='utf8') as file:
    res = csv.reader(file)

    names = []

    for row in res:
        names.append(row[1].capitalize())
    
    modes = statistics.multimode(names)

    print(*sorted(modes))