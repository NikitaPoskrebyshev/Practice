def attack_up(gold, lvl):
    cost = 10 * lvl
    if gold < cost:
        print('вам не хватает золота')
    else:
        lvl += 1
        Attack_up = 1
        return cost, lvl, Attack_up