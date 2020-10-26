n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [i for i in a if i >= 0]
ans = 0
for i in range(m):
    try:
        ans += max(b)
        b.pop(b.index(max(b)))
    except:
        break
print(ans)