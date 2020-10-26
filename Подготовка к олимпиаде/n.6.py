letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
try:
    a, b = input().split('-')
except:
    print('ERROR')
    exit()
an = int(a[1:])
bn = int(b[1:])
aw = a[:1]
bw = b[:1]
if not 0 < an < 9 or not 0 < bn < 9 or aw not in letters or bw not in letters:
    print('ERROR')
elif abs(an - bn) == 2 and abs(letters.index(aw) - letters.index(bw)) == 1:
    print('YES')
elif abs(an - bn) == 1 and abs(letters.index(aw) - letters.index(bw)) == 2:
    print('YES')
else:
    print('NO')