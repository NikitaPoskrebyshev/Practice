import pygame as pg
from random import randint as rn
pg.init()
fps = 60
width = 500
height = 500
clock = pg.time.Clock()
wind = pg.display.set_mode([width, height])
blue = (0, 191, 255)
black = (0, 0, 0)
x = 1
y = 1
while True:
    # a = 1
    # b = 1
    a = rn(1, 5)
    b = rn(1, 5)
    while True:
        wind.fill(black)
        pg.draw.rect(wind, blue, (x, y, 4, 4))
        pg.display.update()
        clock.tick(fps)
# если задевает правую или нижнюю стенку
        if x >= width or y >= height:
            if x >= width and y <= height:
                b = rn(-5, 5)
                a = rn(-10, -5)
            elif y >= height and x <= width:
                a = rn(-5, 5)
                b = rn(-10, -5)
            elif x >= width and y >= height:
                a = rn(-10, -5)
                b = rn(-10, -5)
            while True:
                x += a; y += b
                wind.fill(black)
                pg.draw.rect(wind, blue, (x, y, 4, 4))
                pg.display.update()
                clock.tick(fps)
                if x <= 0 or y <= 0:
                    break
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()
# если задевает верхнюю или левую стенку
        if x <= 0 or y <= 0:
            if x <= 0 and y >= 0:
                a = rn(1, 5)
            elif y <= 0 and x >= 0:
                b = rn(1, 5)
            while True:
                x += a; y += b
                wind.fill(black)
                pg.draw.rect(wind, blue, (x, y, 4, 4))
                pg.display.update()
                clock.tick(fps)
                if x >= 0 or y >= 0:
                    break
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()
        else:
            x += a; y += b
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()