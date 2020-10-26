n = int(input())
a = []
sm = 0
for i in range(n):
    k = int(input())
    for g in range(k):
        a.append(input().split())
    sm += k
for i in range(len(a)):
    a[i][0] = float(a[i][0])
a.sort(reverse=True)
print(sm)
for i in a:
    print('{:.2f}'.format(i[0]), i[1])