import pygame as pg
pg.init()
fps = 300
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
while True:
    buttons = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    wind.fill(black)
    pg.draw.rect(wind, color, (w, h, 100, 50))
    clock.tick(fps)
    pg.display.update()
    if buttons[0]:
        if w <= pos[0] <= w + 100 and h <= pos[1] <= h + 50:
            w = pos[0] - 50; h = pos[1] - 25
            pg.mouse.set_visible(False)
    else:
        color = white
        pg.mouse.set_visible(True)
    for event in pg.event.get():
        # if event.type == pg.MOUSEBUTTONDOWN:
            # if event.button == 1:
            #     color = gray
            # if event.button == 2:
            #     print('колесико')
            # if event.button == 3:
            #     print('пкм')
            # if event.button == 4:
            #     print('колесико вверх')
            # if event.button == 5:
            #     print('колесико вниз')
        if event.type == pg.QUIT:
            exit()