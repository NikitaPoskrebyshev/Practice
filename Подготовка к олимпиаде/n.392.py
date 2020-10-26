n = int(input())
a = input().split()
i = a.index('1')
print(' '.join(a[i:]) + ' ' + ' '.join(a[:i]))