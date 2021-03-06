import pygame as pg
import os
from PyGame.StartMenu import Gold
from PyGame.StartMenu import Dmg
from PyGame.StartMenu import AttackUpgrade
from PyGame.StartMenu import Lvl
from PyGame.StartMenu import Dmgpersecond

##########################################
pg.init()
fps = 60
clock = pg.time.Clock()
##########################################
x = 500
y = 500
ft = pg.font.SysFont('B52 обычный', 60)
ft2 = pg.font.SysFont('B52 обычный', 36)
ft3 = pg.font.SysFont('B52 обычный', 24)
wind = pg.display.set_mode((x, y))
# ИНДИКАТОР ХП
wind_indicator_hp = pg.Surface((100, 50))
# КНОПКА АПГРЕЙДА
wind_upgrade = pg.Surface((50, 50))
# МОНСТР
wind_monster = pg.Surface((300, 100))
# СЛЕДЫ ОТ УДАРОВ
damage_hits = pg.Surface((100, 100))
# СООБЩЕНИЕ О СМЕРТИ МОБА
wind_mob_dead = pg.Surface((250, 75))
# КНОПКА УВЕЛИЧЕНИЯ УРОНА НА ВРЕМЯ
wind_rage = pg.Surface((50, 50))
# КНОПКА УВЕЛИЧЕНИЯ ПАССИВНОГО УРОНА
wind_dmg_per_second = pg.Surface((50, 50))
########################################## ЦВЕТА
white = (255, 255, 255)
black = (000, 000, 000)
green = (0, 200, 64)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
crimson = (220, 20, 60)
color = white
color2 = gray
color3 = gray
##########################################
lvl = Lvl.lvl_load()
########################################## КЛАССЫ / ФУНКЦИИ
class Mob():
    def __init__(self, hp=10):
        self.hp = hp

    def __del__(self):
        pass
class variable():
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def load(self):
        if os.path.exists('Saves/' + self.name):
            a = open('Saves/' + self.name, 'r')
            g = int(a.read())
            a.close()
            self.value = g
        else:
            b = open('Saves/' + self.name, 'w')
            b.write(str(self.value))
            b.close()


    def save(self):
        a = open('Saves/' + self.name, 'w')
        a.write(str(n))
        a.close()
        print('Данные сохранены')
class game_object():
    def __init__(self, width, height, color = None):
        self.width = width
        self.height = height
        self.color = color
        self.wind = pg.Surface((self.width, self.height))
        if self.color:
            self.wind.fill(self.color)
# test = game_object(50, 50, green)
# test1 = game_object(50, 50)
def draw(type, x = 0, y = 0, width = 0, height = 0):
    if type == 'monster':
        pg.draw.rect(wind_monster, color, (x, y, width, height))
        wind.blit(wind_monster, (100, 200))
        if mobdead:
            wind_monster.fill(black)
            t = ft.render('Mob is dead', 1, red)
            wind_monster.blit(t, (30, 30))
            wind.blit(wind_monster, (100, 200))
            wind_monster.fill(black)
    if type == 'button':
        pg.draw.rect(wind_upgrade, color2, (x, y, width, height))
        wind.blit(wind_upgrade, (350, 350))
        if mobdead:
            wind_upgrade.fill(black)
            wind.blit(wind_upgrade, (350, 350))
    if type == 'hits':
        pg.draw.lines(damage_hits, black, False,
                      ([event.pos[0] - 6, event.pos[1] - 6], [event.pos[0] + 6, event.pos[1] + 6]), 5)
        pg.draw.lines(damage_hits, black, False,
                      ([event.pos[0] - 6, event.pos[1] + 6], [event.pos[0] + 6, event.pos[1] - 6]), 5)
        pg.draw.lines(damage_hits, white, False,
                      ([event.pos[0] - 5, event.pos[1] - 5], [event.pos[0] + 5, event.pos[1] + 5]), 2)
        pg.draw.lines(damage_hits, white, False,
                      ([event.pos[0] - 5, event.pos[1] + 5], [event.pos[0] + 5, event.pos[1] - 5]), 2)
        wind_monster.blit(damage_hits, (-200, -200))
    if type == 'rage':
        pg.draw.rect(wind_rage, red, (0, 5, 50, 40))
        pg.draw.rect(wind_rage, red, (5, 0, 40, 50))
        wind.blit(wind_rage, (350, 225))
        if mobdead:
            wind_rage.fill(black)
            wind.blit(wind_rage)
    if type == 'dmg_button':
        wind_dmg_per_second.fill(color3)
        t = ft3.render('dps', 1, black)
        wind_dmg_per_second.blit(t, (20, 20))
        wind.blit(wind_dmg_per_second, (350, 225))
    return type, x, y, width, height


location_level = 1
mb = Mob(location_level * 10)
mb.hp = 10 * lvl


def start_load():
    draw('monster', 100, 0, 100, 100)
    draw('button', width = 50, height = 50)
    draw('dmg_button')
    # wind.blit(test.wind, (10, 10))
    # wind.blit(test1.wind, (70, 10))
    current_hp()


def current_hp():
    wind_indicator_hp.fill(black)
    wind.blit(wind_indicator_hp, (225, 415))
    t4 = ft2.render(str(mb.hp) + ' hp', 0, white)
    wind_indicator_hp.blit(t4, (0, 0))
    wind.blit(wind_indicator_hp, (225, 415))
    if mobdead:
        wind_indicator_hp.fill(black)
        wind.blit(wind_indicator_hp, (225, 415))
    pg.display.update()
    # def damage_hits():
    #     pg.draw.lines(damage_hits, black, False,
    #                   ([event.pos[0] - 6, event.pos[1] - 6], [event.pos[0] + 6, event.pos[1] + 6]), 5)
    #     pg.draw.lines(damage_hits, black, False,
    #                   ([event.pos[0] - 6, event.pos[1] + 6], [event.pos[0] + 6, event.pos[1] - 6]), 5)
    #     pg.draw.lines(damage_hits, white, False,
    #                   ([event.pos[0] - 5, event.pos[1] - 5], [event.pos[0] + 5, event.pos[1] + 5]), 2)
    #     pg.draw.lines(damage_hits, white, False,
    #                   ([event.pos[0] - 5, event.pos[1] + 5], [event.pos[0] + 5, event.pos[1] - 5]), 2)
    #     wind.blit(damage_hits, (200, 200))


##########################################
n = 0
a = 0
location_mob_kill = 0
mobdead = False
testflag = False
##########################################
gold = Gold.gold()
dmg = Dmg.dmg()
dmg_per_second = Dmgpersecond.dmg_per_second()
dps_lvl = Dmgpersecond.dps_lvl()
##########################################


while True:
    start_load()
    pg.display.update()
    if mobdead and n == 1000:
        mb = Mob(lvl * 10)
        mobdead = False
        wind.fill(black)
        n = 0
        draw('monster', 100, 0, 100, 100)
        wind.blit(wind_monster, (200, 200))
    elif mobdead:
        n += 1
        continue
    if dmg_per_second > 0 and a % fps == 0 and not mobdead:
        mb.hp -= dmg_per_second
        a = 0
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
                    draw('monster', 100, 0, 100, 100)
                    draw('hits', 0, 0, 100, 100)
                    # damage_hits()
                    mb.hp -= dmg
                    current_hp()

                    # кнопка квеличения урона на время
                    # if a % 1 == 0:
                    #     draw('rage', 0, 0, 0, 0)
                    #     testflag = True
                    #
                    # if 350 <= event.pos[0] <= 400 and 225 <= event.pos[1] <= 275 and testflag:
                    #     dmg *= 5



                # upgrade
                if 350 <= event.pos[0] <= 400 and 350 <= event.pos[1] <= 400:
                    try:
                        buf = AttackUpgrade.attack_up(gold, lvl)
                        dmg += buf[2]
                        gold -= buf[0]
                        lvl = buf[1]
                    except:
                        pass
                    wind.fill(black)
                    color2 = gray
                    draw('button', 0, 0, 50, 50)
                elif 350 <= event.pos[0] <= 400 and 225 <= event.pos[1] <= 275:
                    try:
                        buf = AttackUpgrade.dps(gold, dps_lvl)
                        dmg_per_second += buf[2]
                        gold -= buf[0]
                        dps_lvl = buf[1]
                    except:
                        pass
                    wind.fill(black)
                    color3 = gray
                    draw('dmg_button')

            # смерть монстра
            if mb.hp <= 0 and not mobdead:
                mobdead = True
                wind.fill(black)
                gold += lvl
                location_mob_kill += 1
                if location_mob_kill == 10:
                    lvl += 1
                    location_mob_kill = 0

        if event.type == pg.MOUSEBUTTONUP:
            # анимация удара
            if event.button == 1 and not mobdead:
                color = white
                draw('monster', 100, 0, 100, 100)
        if event.type == pg.QUIT:
            Gold.gold_write(gold)
            Dmg.dmg_write(dmg)
            Lvl.lvl_save(lvl)
            # Dmgpersecond.dmg_per_second_write(dmg_per_second)
            # Dmgpersecond.dps_lvl_save(dps_lvl)
            exit()
    if gold >= 10 * lvl:
        color2 = yellow
    if gold >= 50 * dps_lvl:
        color3 = red
    a += 1
    clock.tick(fps)
