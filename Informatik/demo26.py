n = int(input("Введите количество элементов последовательности: "))
s = 0

for i in range(n):
 e = int(input())
 if (e % 7 == 1):
  s = s + e

print(s)