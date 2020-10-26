a, b = map(int, input().split())
ab = a * b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(ab//(max(a, b)))