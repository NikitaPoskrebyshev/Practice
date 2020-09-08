from random import randint
def Registration():
    print("Для регистрации введите необходимые данные")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    middlename = input("Отчество: ")
    login = (name[0] + surname[:3])
    while len(login) < 6:
        login += str(randint(0, 9))
    print("Ваш логин:", login)
    password = input("Придумайте пароль: ")
    a = False
    while True:
        length = len(password)
        if length < 5:
            print("Длина пароля должна быть не менее 5 символов")
            password = input()
        elif " " in password:
            print("Пароль не должен содержать пробелы")
            password = input()
        else: a = True; print("Данные успешно сохранены")
        if a:
            break
    archive = open(login + ".reg", "w")
    archive.write("Фамилия: " + surname + "\n" + "Имя: " + name + "\n" + "Отчество: " + middlename + "\n" + "Логин: " + login + "\n" + "Пароль: " + str(password))
