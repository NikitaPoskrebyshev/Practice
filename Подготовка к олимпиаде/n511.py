n = int(input())
x = 0
y = 5
if n > 145:
    print('NO')
    exit()
elif n == 1:
    print(0, 0)
    exit()
elif n == 2:
    print(0, 5)
    exit()
for i in range(1, n - 1):
    y += 5
    n -= 1
    if y == 60:
        x += 1
        y = 0
print(x, y)