import csv

with open('students.csv', newline='', encoding='utf8') as file:
    res = csv.reader(file)

    for row in res:
        if 'Бороденков' in row:
            print(row)