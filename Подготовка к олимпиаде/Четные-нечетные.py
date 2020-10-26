A = int(input())
B = int(input())
s = 0
for i in range(A, B + 1):
    if i % 2 == 0:
        s += i
    else:
        s += i
answer = s
print(answer)