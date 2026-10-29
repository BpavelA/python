c = 0
m = int(input())
while m != 0:
 m = int(input())
 if (m % 8 == 5) and (511 < m < 4096):
  c += 1
print(c)
