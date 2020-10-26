a = list(map(int, list(input())))
k = 0
mi = 0
ma = 0
for i in a:
    if i == 1:
        k += 1
    else:
        k -= 1
    if k > ma:
        ma = k
    if k < mi:
        mi = k
print(1 + ma + abs(mi))