from random import randint
def Human():
    score = 10
    b = -1
    a = randint(0, 100)
    while a != b:
        b = int(input("Введите Ваше число: "))
        if a > b:
            print(">")
        elif a < b:
            print("<")
        score -= 1
    if score < 0:
        score = 0
    print("Вы угадали число!")
    return score





