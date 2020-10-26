m = int(input())
for i in range(m):
    if m % (i * 2 + 1) == 0:
        print(i)