n, s = map(int, input().split())
a = list(map(int, input().split()))
sm = 0
x = 0
for i in range(n):
    idx = min(a)
    if sm + idx <= s:
        sm += idx
        dl = a.index(idx)
        a.pop(dl)
        x += 1
        print(a)
print(x)