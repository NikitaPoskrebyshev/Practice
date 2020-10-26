N, M = map(int, input().split())
x = N // M
if N%M == 0:
    print((str(N//M)+' ')*M)
elif N%M == 1:
    print((str(x)+" ")*(M-1),x+1,sep='')
elif N%M > 1:
    x_p = x + 1
    x_n = x - 1
    for i in range(M):
        if x * (M - i) + x_p * i == N:
            print((str(x) + ' ') * (M - i), (str(x_p) + ' ') * i, sep= '')
            break
        elif x * (M - i) + x_n * i == N:
            print((str(x) + ' ') * (M - i), (str(x_n) + ' ') * i, sep= '')
            break