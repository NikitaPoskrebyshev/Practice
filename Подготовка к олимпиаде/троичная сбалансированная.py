a = int(input())
m = []
if a < 0:
    negative = True
    a = abs(a)
else:
    negative = False
while a != 0:
    m.append(a % 3)
    a //= 3
m.append(0)
for i in range(len(m)):
    if m[i] == 3:
        m[i] = 0
        m[i + 1] += 1
    elif m[i] == 2:
        m[i] = 'z'
        m[i + 1] += 1
m = list(reversed(m))
if negative:
    for i in range(len(m)):
        if m[i] == 1:
            m[i] = 'z'
        elif m[i] == 'z':
            m[i] = 1
if m[0] == 0:
    m.pop(0)
l = ''
for i in m:
    l += str(i)
print(l)