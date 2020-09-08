def InvDigits(a):
    a = str(a)
    b = ""
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    return(b)
print(InvDigits(1234))