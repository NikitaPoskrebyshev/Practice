n = int(input())
sum = 0
a = n
if n < 0:
    n = n*(-1)
for i in range(n + 1):
    sum += i
if a <= 0:
    print(sum*(-1) + 1)
else:
    print(sum)