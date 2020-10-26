a = []
k = 0
n, m = map(int, input().split())
a.append('.' * (m + 2))
for i in range(n):
    a.append(list('.' + input() + '.'))
a.append('.' * (m + 2))
for i in range(1, n + 1):
    for g in range(1, m + 1):
        if a[i][g] == a[i + 1][g] == a[i][g + 1] == a[i - 1][g] == a[i][g - 1] == '.':
            k += 1
print(k)