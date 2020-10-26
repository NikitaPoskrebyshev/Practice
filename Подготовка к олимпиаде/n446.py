def check(t, a):
    if t == 0:
        if a != '.':
            print('NO')
            exit()
    elif t == 1:
        if a != '.' and a != 'B':
            print('NO')
            exit()
    elif t == 2:
        if a != '.' and a != 'G':
            print('NO')
            exit()
    elif t == 3:
        if a != '.' and a != 'B' and a != 'G':
            print('NO')
            exit()
    elif t == 4:
        if a != '.' and a != 'R':
            print('NO')
            exit()
    elif t == 5:
        if a != '.' and a != 'R' and a != 'B':
            print('NO')
            exit()
    elif t == 6:
        if a != '.' and a != 'R' and a != 'G':
            print('NO')
            exit()
    elif t == 7:
        if a != '.' and a != 'R' and a != 'G' and a != 'B':
            print('NO')
            exit()

n, m = map(int, input().split())
tb = []
adv = []
for i in range(n):
    adv.append(list(map(str, input())))
for i in range(n):
    tb.append(list(map(int, input().split())))
for i in range(n):
    for k in range(m):
        t = tb[i][k]
        a = adv[i][k]
        check(t, a)
print('YES')