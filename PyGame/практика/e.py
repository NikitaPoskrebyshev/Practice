import pygame as pg
from random import randint as rn
pg.init()
wind = pg.display.set_mode([825, 540])
white = (255, 255, 255)
black = (000, 000, 000)
green = (0, 200, 64)
yellow = (255, 255, 0)
red = (255, 0, 0)
gray = (125, 125, 125)
x1 = red
x2 = yellow
x3 = green
fps = 30
clock = pg.time.Clock()
n = 0
f = 0
while True:
    clock.tick(fps)
    if n % 15 in [0, 1, 2]:
        x1, x2, x3 = red, gray, gray
    elif n % 15 in [3]

    elif n % 9 in [3, 4, 5]:
        x1, x2, x3 = gray, yellow, gray
    else:
        x1, x2, x3 = gray, gray, green
    pg.draw.circle(wind, x1, (250, 100), 50)
    pg.draw.circle(wind, x2, (250, 200), 50)
    pg.draw.circle(wind, x3, (250, 300), 50)
    pg.display.update()
    pg.display.set_caption(str(n))
    f += 1
    if f == 30:
        n += 1
        f = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
