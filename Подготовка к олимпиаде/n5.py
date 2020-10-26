n = int(input())
a = list(map(int, input().split()))
chet = []
nechet = []
for i in a:
    if i % 2 == 1:
        nechet.append(i)
    else:
        chet.append(i)
for i in nechet:
    print(i, ' ', end='')
print()
for i in chet:
    print(i, ' ', end='')
print()
if len(chet) < len(nechet):
    print('NO')
else:
    print('YES')