n, d = map(int, input().split())
a = list(map(int, input().split()))
l = 0
for i in range(len(a) - 1):
    l += (abs(a[i] - a[i + 1]) ** 2 + d ** 2) ** 0.5
print(round(l, 6))