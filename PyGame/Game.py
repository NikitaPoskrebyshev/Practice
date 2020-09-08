import pygame as pg
from PyGame.StartMenu import Gold
from PyGame.StartMenu import Dmg
from PyGame.StartMenu import AttackUpgrade
from PyGame.StartMenu import Lvl
##########################################
pg.init()
fps = 60
clock = pg.time.Clock()
##########################################
x = 500
y = 500
ft = pg.font.SysFont('arial', 60)
ft2 = pg.font.SysFont('B52 Ó·˚˜Ì˚È', 36)
wind = pg.display.set_mode((x, y))
# »Õƒ» ¿“Œ– ’œ
wind_indicator_hp = pg.Surface((50, 50))
#  ÕŒœ ¿ ¿œ√–≈…ƒ¿
wind_upgrade = pg.Surface((50, 50))
# ÃŒÕ—“–
wind_monster = pg.Surface((100, 100))
########################################## ÷¬≈“¿
white = (255, 255, 255)
black = (000, 000, 000)
green = (0, 200, 64)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
##########################################  À¿——€
class Mob():
    def __init__(self, hp = 10):
        self.hp = hp
    def __del__(self):
        pass
##########################################
color = white
color2 = gray
n = 0
a = 0
location_level = 1
location_mob_kill = 0
mobdead = False
mb = Mob(location_level * 10)
testflag = False
##########################################
gold = Gold.gold()
dmg = Dmg.dmg()
lvl = Lvl.lvl_load()
##########################################