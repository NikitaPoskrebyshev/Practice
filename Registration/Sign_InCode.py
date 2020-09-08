from os.path import exists
a = 0
SignInLogin = input("Введите Ваш логин: ")
while not exists(SignInLogin + ".reg"):
    print("Данного логина не существует")
    SignInLogin = input("Введите Ваш логин: ")
checkfile = open(SignInLogin + ".reg", "r")
Data = []
for i in checkfile:
    Data.append(i)
TruePassword = Data[4][8:]
while a != 3:
    SignInpassword = input("Введите ваш пароль: ")
    a += 1
    if SignInpassword == TruePassword:
        print("Успешный вход!")
        break
    else:
        print("Неправильный пароль! Количество оставшихся попыток:", 3 - a)
    if a == 3:
        print("Доступ к аккаунту ограничен на 15 минут!")
        exit()


