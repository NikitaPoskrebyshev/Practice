import pygame as pg
pg.init()
fps = 60
x = 500
y = 500
white = (255, 255, 255)
gray = (125, 125, 125)
black = (0, 0, 0)
red = (255, 0, 0)
wind = pg.display.set_mode((x, y))
clock = pg.time.Clock()
color = white
while True:
    # buttons = pg.mouse.get_pressed()
    # pos = pg.mouse.get_pos()
    # wind.fill(black)
    clock.tick(fps)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for object_y in range(500, event.pos[1], -1):
                    clock.tick(fps + 60)
                    wind.fill(black)
                    pg.draw.aalines(wind, color, True, ([event.pos[0], object_y], [event.pos[0] - 5, object_y + 10], [event.pos[0] + 5, object_y + 10]))
                    pg.display.update()
                wind.fill(black)
                pg.draw.line(wind, red, [event.pos[0], object_y + 10], [event.pos[0], object_y - 10])
                pg.draw.line(wind, red, [event.pos[0] - 10, object_y], [event.pos[0] + 10, object_y])
                pg.draw.line(wind, red, [event.pos[0] - 7, object_y - 7], [event.pos[0] + 7, object_y + 7])
                pg.draw.line(wind, red, [event.pos[0] - 7, object_y + 7], [event.pos[0] + 7, object_y - 7])
        if event.type == pg.QUIT:
            exit()