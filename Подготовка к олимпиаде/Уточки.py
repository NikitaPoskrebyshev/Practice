a = int(input())
b = int(input())
answer = 1
while answer % a != 1 or answer % b != (b - 1):
    answer += 1
print(answer)