n = int(input())
for i in range(n):
    a = input()
    b = a
    x1 = a[0:3]
    x2 = int(a[3:])
    x2_n = str(x2 - 1)
    x2_p = str(x2 + 1)
    if len(x2_n) < 3:
        x2_n += '0'*(3 - len(x2_n))
    if len(x2_p) < 3:
        x2_p += '0'*(3 - len(x2_p))
    sum1 = int(x1[0]) + int(x1[1]) + int(x1[2])
    sum2_n = int(x2_n[0]) + int(x2_n[1]) + int(x2_n[2])
    sum2_p = int(x2_p[0]) + int(x2_p[1]) + int(x2_p[2])
    if sum1 - sum2_n == 0 or sum1 - sum2_p == 0:
        print('Yes')
    else:
        print('No')