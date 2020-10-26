import os
def dmg_per_second():
    if os.path.exists('Saves/dmg_per_second'):
        a = open('Saves/dmg_per_second', 'r')
        d = int(a.read())
        a.close()
        return d
    else:
        b = open('Saves/dmg_per_second', 'w')
        b.write('0')
        b.close()
        return 1
def dmg_per_second_write(n):
    a = open('Saves/dmg_per_second', 'w')
    a.write(str(n))
    a.close()
def dps_lvl():
    if os.path.exists('Saves/dps_lvl'):
        a = open('Saves/dps_lvl', 'r')
        d = int(a.read())
        a.close()
        return d
    else:
        b = open('Saves/dps_lvl', 'w')
        b.write('0')
        b.close()
        return 1
def dps_lvl_save(n):
    a = open('Saves/dps_lvl', 'w')
    a.write(str(n))
    a.close()