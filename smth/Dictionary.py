documents = [
{"type": "passport","number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice","number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance","number": "10006", "name": "Аристарх Павлов"}]

dirictories = {
    '1': ['2207 876234','11-2','5455 028765'],
    '2': ['10006'],
    '3': []
}
def people():
    number = input()
    for doc in documents:
        if number == doc["number"]:
            print(doc["name"])
            break
# people()
def shelf():
    number = input()
    for dir in dirictories:
        if number in dirictories[dir]:
            print(dir)
            break
    else: print("Такого документа не было найдено.")
shelf()
def l():
    for doc in documents:
        a = list(doc.values())
        print(a[0], '"' + a[1] + '"', '"' + a[2] + '"')
# l()
def listing():
    for slovar in documents:
        print(" ".join(list(slovar.values())))

def add():
    type = input()
    number = input()
    name = input()
    dirictory = input()
    if not (number in list(dirictories.keys())):
        print("Такой полки не существует.")
        exit()
    a = {"type": type, "number": number, "name": name}
    documents.append(a)
    dirictories[dirictory].append(number)
# add()
# print(dirictories)
shelf()