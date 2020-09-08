from random import randint
class warrior:
    hp = 100
    dmg = 20
class unit1(warrior):
    pass
class unit2(warrior):
    pass
a = True
while True:
    b = randint(1, 2)
    if b == 1:
        unit1.hp -= unit2.dmg
        print("unit2 attacked unit1, now unit1 has", unit1.hp, "hp")
    else:
        unit2.hp -= unit1.dmg
        print("unit1 attacked unit2, now unit2 has", unit2.hp, "hp")
    if unit1.hp <= 0:
        print("unit2 wins!")
        break
    elif unit2.hp <= 0:
        print("unit1 wins!")
        break