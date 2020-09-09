import os
def lvl_load():
    if os.path.exists('Saves/lvl'):
        a = open('Saves/lvl', 'r')
        d = int(a.read())
        a.close()
        return d
    else:
        b = open('Saves/lvl', 'w')
        b.write('1')
        b.close()
        return 1
def lvl_save(n):
    a = open('Saves/lvl', 'w')
    a.write(str(n))
    a.close()
    print('Данные сохранены')
