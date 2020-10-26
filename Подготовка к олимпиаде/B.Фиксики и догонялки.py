n = int(input())
a = []
t = 1
x = 0
y = 0
x1 = 0
y1 = 0
ans = 0
mx = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    m = max(a[i])
    if m > mx:
        mx = m
for h in range(mx):
    for i in a:
        for g in i:
            if g == t:
                x = i.index(g) + 1
                y = a.index(i) + 1
                t += 1
                if t > 2:
                    ans += abs(x1 - x) + abs(y1 - y)
                x1, y1 = x, y
                x, y = 0, 0
    if t > mx:
        print(ans)
        exit()