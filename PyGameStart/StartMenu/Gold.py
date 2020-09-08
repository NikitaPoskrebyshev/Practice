import os
def gold():
    if os.path.exists('Saves/gold'):
        a = open('Saves/gold', 'r')
        g = int(a.read())
        a.close()
        return g
    else:
        b = open('Saves/gold', 'w')
        b.write('0')
        b.close()
        return 0
def goldwrite(n):
    a = open('Saves/gold', 'w')
    a.write(str(n))
    a.close()
    print('Данные сохранены')