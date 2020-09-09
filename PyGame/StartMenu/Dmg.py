import os
def dmg():
    if os.path.exists('Saves/dmg'):
        a = open('Saves/dmg', 'r')
        d = int(a.read())
        a.close()
        return d
    else:
        b = open('Saves/dmg', 'w')
        b.write('1')
        b.close()
        return 1
def dmg_write(n):
    a = open('Saves/dmg', 'w')
    a.write(str(n))
    a.close()
    print('Данные сохранены')