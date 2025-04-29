#numbers = list(map(lambda x: tuple(str(x)), list(range(int(input()), int(input()) + 1))))
numbers = list(filter(lambda x: x % 10 != 0, range(int(input()), int(input()) + 1)))
print(numbers)
#print(filter(all(map(lambda y: (lambda x: x % y == 0, y), numbers), numbers)