n, bx, by, l = map(int, input().split())
id = 0
for i in range(n):
    x, y = map(int, input().split())
    id += 1
    c = (abs(bx - x) ** 2 + abs(by - y) ** 2) ** 0.5
    if l >= c:
        print(id)
        break
else:
    print('Yes')