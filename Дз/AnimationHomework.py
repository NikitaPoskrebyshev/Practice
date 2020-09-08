import pygame as pg
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
    wind.fill(black)
    pg.draw.rect(wind, blue, (x, y, 4, 4))
    pg.display.update()
    clock.tick(fps)
    if x >= width:
        for i in range(width):
            x -= 1
            y -= 1
            wind.fill(black)
            pg.draw.rect(wind, blue, (x, y, 4, 4))
            pg.display.update()
            clock.tick(fps)
            if x <= 0 or y <= 0:
                break
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
    else:
        x += 1; y += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()