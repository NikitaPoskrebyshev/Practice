import pygame as pg
from PyGame.StartMenu import Gold
from PyGame.StartMenu import Dmg
from PyGame.StartMenu import AttackUpgrade
##########################################
pg.init()
fps = 60
clock = pg.time.Clock()
########################################## 
x = 500
y = 500
ft = pg.font.SysFont('arial', 60)
ft2 = pg.font.SysFont('B52 обычный', 36)
wind = pg.display.set_mode((x, y))
wind_indicator_hp = pg.Surface((50, 50))
wind_upgrade = pg.Surface((50, 50))
##########################################  ЦВЕТА
white = (255, 255, 255)
black = (000, 000, 000)
green = (0, 200, 64)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
##########################################
color = white
color2 = gray
n = 0
a = 0
lvl = 1
location_level = 1
location_mob_kill = 0
mobdead = True
##########################################
# загрузка данных
gold = Gold.gold()
dmg = Dmg.dmg()
##########################################
def damage():
    damage_indicate = pg.Surface((100, 100))
    pg.draw.lines(damage_indicate, black, False, ([event.pos[0] - 6, event.pos[1] - 6], [event.pos[0] + 6, event.pos[1] + 6]), 5)
    pg.draw.lines(damage_indicate, black, False, ([event.pos[0] - 6, event.pos[1] + 6], [event.pos[0] + 6, event.pos[1] - 6]), 5)
    pg.draw.lines(damage_indicate, white, False,
                  ([event.pos[0] - 5, event.pos[1] - 5], [event.pos[0] + 5, event.pos[1] + 5]), 2)
    pg.draw.lines(damage_indicate, white, False,
                  ([event.pos[0] - 5, event.pos[1] + 5], [event.pos[0] + 5, event.pos[1] - 5]), 2)
    wind.blit(damage_indicate, (200, 200))
class Mob():
    def __init__(self, hp = 10):
        self.hp = hp
    def __del__(self):
        pass
while True:
    pg.display.update()
    pg.draw.rect(wind, color2, (350, 350, 50, 50))
    if mobdead and n == 30:
        mb = Mob(location_level * 10)
        mobdead = False
        wind.fill(black)
        n = 0
        pg.draw.rect(wind, white, (200, 200, 100, 100))
    elif mobdead:
        n += 1
        continue
    t2 = ft2.render('gold: ' + str(gold), 0, white)
    t3 = ft2.render(str(location_mob_kill) + ' из 10', 0, white)
    t5 = ft2.render('damage: ' + str(dmg), 0, white)
    wind.blit(t2, (400, 50))
    wind.blit(t3, (212, 150))
    wind.blit(t5, (20, 450))



    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
            # удар по монстру
                if 200 <= event.pos[0] <= 300 and 200 <= event.pos[1] <= 300 and not mobdead:
                    color = red
                    pg.draw.rect(wind, color, (200, 200, 100, 100))
                    damage()
                    mb.hp -= dmg
                    wind_indicator_hp.fill(black)
                    wind.blit(wind_indicator_hp, (225, 415))
                    t4 = ft2.render(str(mb.hp) + ' hp', 0, white)
                    wind_indicator_hp.blit(t4, (0, 0))
                    wind.blit(wind_indicator_hp, (225, 415))

                # if a % 10 == 0:
                #     pg.draw.rect
                #
                # if 350 <= event.pos[0] <= 400 and 275 <= event.pos[1] <= 325 and check == 1:
                #


            # upgrade
                elif 350 <= event.pos[0] <= 400 and 350 <= event.pos[1] <= 400:
                    try:
                        buf = AttackUpgrade.attack_up(gold, lvl)
                        dmg += buf[2]
                        gold -= buf[0]
                        lvl = buf[1]
                        print(buf)
                    except:
                        pass
                    wind.fill(black)
                    color2 = gray
                    pg.draw.rect(wind, color2, (350, 350, 50, 50))



            # смерть монстра
            if mb.hp <= 0 and not mobdead:
                mobdead = True
                wind.fill(black)
                t = ft.render('Mob is dead', 1, red)
                wind.blit(t, (100, 200))
                gold += lvl
                location_mob_kill += 1
                if location_mob_kill == 10:
                    location_level += 1
                    location_mob_kill = 0



        if event.type == pg.MOUSEBUTTONUP:
        # анимация удара
            if event.button == 1 and not mobdead:
                color = white
                pg.draw.rect(wind, color, (200, 200, 100, 100))
        if event.type == pg.QUIT:
            Gold.goldwrite(gold)
            Dmg.dmgwrite(dmg)
            exit()
    if gold >= 10 * lvl:
        color2 = yellow
    a += 1
    clock.tick(fps)