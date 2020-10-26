a = []
k = 0
n, m = map(int, input().split())
for i in range(n):
    a.append(list(input()))
for i in range(n):
    for g in range(m):
        if i == 0:
            if g == 0:
                if a[i][g] == a[i + 1][g] == a[i][g + 1] == '.':
                    k += 1
            elif g == m - 1:
                if a[i][g] == a[i + 1][g] == a[i][g - 1] == '.':
                    k += 1
            elif 0 < g < m - 1:
                if a[i][g] == a[i + 1][g] == a[i][g + 1] == a[i][g - 1] == '.':
                    k += 1
        elif i == n - 1:
            if g == 0:
                if a[i][g] == a[i][g + 1] == a[i - 1][g] == '.':
                    k += 1
            elif g == m - 1:
                if a[i][g] == a[i - 1][g] == a[i][g - 1] == '.':
                    k += 1
            elif 0 < g < m - 1:
                if a[i][g] == a[i - 1][g] == a[i][g - 1] == a[i][g + 1] == '.':
                    k += 1
        elif 0 < i < n - 1:
            if g == 0:
                if a[i][g] == a[i][g + 1] == a[i - 1][g] == a[i + 1][g] == '.':
                    k += 1
            elif g == m - 1:
                if a[i][g] == a[i - 1][g] == a[i][g - 1] == a[i + 1][g] == '.':
                    k += 1
            elif 0 < g < m - 1:
                if a[i][g] == a[i - 1][g] == a[i][g - 1] == a[i][g + 1] == a[i + 1][g] == '.':
                    k += 1
print(k)