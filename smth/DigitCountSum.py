def DigitCountSum(a):
    C = len(str(a))
    S = 0
    while a > 0:
        b = a % 10
        S += b
        a = a // 10
    return(C, S)
a = int(input())
b = DigitCountSum(a)
print(b)