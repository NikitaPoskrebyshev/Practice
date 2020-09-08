import pygame as pg
pg.init()
fps = 60
x = 500
y = 500
w = 200
h = 200
white = (255, 255, 255)
gray = (125, 125, 125)
black = (0, 0, 0)
wind = pg.display.set_mode((x, y))
clock = pg.time.Clock()
color = white
a = 1
while True:
    buttons = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if a == 1:
        pg.draw.rect(wind, color, (w, h, 100, 50))
    clock.tick(fps)
    pg.display.update()
    # if w <= pos[0] <= w + 100 and h <= pos[1] <= h + 50 and buttons[0]:
    #     color = gray
    # elif w <= pos[0] <= w + 100 and h <= pos[1] <= h + 50 and buttons[0]:
    #     color = black
    for event in pg.event.get():
        if w <= pos[0] <= w + 100 and h <= pos[1] <= h + 50 and event.type == pg.MOUSEBUTTONDOWN:
            color = gray
        if w <= pos[0] <= w + 100 and h <= pos[1] <= h + 50 and event.type == pg.MOUSEBUTTONUP:
            a = 0
            color = white
            wind.fill(black)
            pg.draw.rect(wind, color, (125, 150, 100, 50))
            pg.draw.rect(wind, color, (275, 150, 100, 50))
            pg.draw.rect(wind, color, (125, 250, 100, 50))
            pg.draw.rect(wind, color, (275, 250, 100, 50))
            pg.draw.rect(wind, color, (425, 25, 50, 50))
        if 425 <= pos[0] <= 475 and 25 <= pos[1] <= 75 and event.type == pg.MOUSEBUTTONDOWN:
            a = 1
            wind.fill(black)
        if event.type == pg.QUIT:
            exit()

