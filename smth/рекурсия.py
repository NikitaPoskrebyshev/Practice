def rec(n):
    if n == 1:
        return 1
    elif 1 < n < 2:
        return 0
    else:
        return rec(n / 2)
if rec(129) == 1:
    print('yes')
else:
    print('no')
