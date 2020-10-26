H = int(input())
A = int(input())
B = int(input())
answer = H - A + B
if answer > 23:
    answer -= 24
print(answer)
