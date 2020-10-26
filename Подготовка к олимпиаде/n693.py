a, b = map(list, input().split())
if len(a) != len(b):
    print('No')
    exit()
for i in a:
    if i.isupper():
        t = a.index(i)
        a.pop(a.index(i))
        a.insert(t, i.lower())
for i in b:
    if i.isupper():
        t = b.index(i)
        b.pop(b.index(i))
        b.insert(t, i.lower())
for i in b:
    if i not in a:
        print('No')
        exit()
    else:
        a.pop(a.index(i))
print('Yes')