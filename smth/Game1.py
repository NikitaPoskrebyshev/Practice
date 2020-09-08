from random import randint
def Robot(nickname):
    print('играет:', nickname)
    x = int(input("Введите загаданное число: "))
    score = 10
    start = 0
    stop = 100
    while True:
        a = randint(start, stop)
        print(a)
        t = input("Угадал?")
        if t == ">":
            start = a + 1
        elif t == "<":
            stop = a - 1
        else:
            print("Ура! Угадал!")
            break
        score -= 1
    if score < 0:
        score = 0
    return score


