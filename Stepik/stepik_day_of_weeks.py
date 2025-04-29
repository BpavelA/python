from datetime import date

d1 = date(2021, 9, 20)
d2 = date(2022, 8, 18)

count = 0

for d_ord in range(d1.toordinal(), d2.toordinal() + 1):
    d = date.fromordinal(d_ord)
    if (d.weekday() == 3):
        count += 1

print(count)