A = int(input())
B = int(input())
N = 0
for i in range(A, B):
    if i % 2 == 0:
        N += 1
print(N)