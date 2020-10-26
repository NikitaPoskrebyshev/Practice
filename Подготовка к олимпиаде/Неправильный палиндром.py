a = input()
for i in range(len(a)):
    t = list(a)
    t.pop(i)
    t = ''.join(t)
    sl = list(reversed(t[len(t)//2:]))
    sl = ''.join(sl)
    if len(t) % 2 != 0:
        sl1 = t[:len(t)//2 + 1]
    else:
        sl1 = t[:len(t)//2]
    if sl == sl1:
        print(i + 1)
        break
else:
    print(0)