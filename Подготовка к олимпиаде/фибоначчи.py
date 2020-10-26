n = int(input())
x1 = 1
x2 = 1
x3 = 0
i = 2
while x3 < n:
    i += 1
    x3 = x1 + x2
    if n == x3:
        print(1)
        print(i)
        exit()
    x1 = x2
    x2 = x3
print(0)