from fractions import Fraction

n = int(input())

lst = set()

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if Fraction(a, b) < 1:
            lst.add(Fraction(a, b))
print(*sorted(lst), sep='\n')