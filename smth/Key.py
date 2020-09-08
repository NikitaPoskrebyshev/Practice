import pygame as pg
pg.init()
fps = 60
x, y = 500, 500
w, h = 250, 250
wind = pg.display.set_mode([x, y])
clock = pg.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color = white
motion = 'stop'
fig = 'circle'
def figure(n):
    if n == 'rect':
        pg.draw.rect(wind, color, ((w - 10), (h - 10), 20, 20))
    elif n == 'circle':
        pg.draw.circle(wind, color, (w, h), 10)
    elif n == 'triangle':
        pg.draw.aalines(wind, color, True, ([w, h - 10], [w + 5, h + 10], [w - 5, h + 10]))
while True:
    figure(fig)
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and keys[pg.K_UP]:
        w -= 3
        h -= 3
    elif keys[pg.K_RIGHT] and keys[pg.K_UP]:
        w += 3
        h -= 3
    elif keys[pg.K_LEFT] and keys[pg.K_DOWN]:
        w -= 3
        h += 3
    elif keys[pg.K_RIGHT] and keys[pg.K_DOWN]:
        w += 3
        h += 3
    elif keys[pg.K_RIGHT]:
        w += 3
    elif keys[pg.K_UP]:
        h -= 3
    elif keys[pg.K_LEFT]:
        w -= 3
    elif keys[pg.K_DOWN]:
        h += 3
    # if motion == 'left':
    #     w -= 3
    # elif motion == 'right':
    #     w += 3
    # elif motion == 'up':
    #     h -= 3
    # elif motion == 'down':
    #     h += 3
    # elif motion == 'upright':
    #     w += 2; h -= 2
    else:
        if w < x // 2:
            w += 1
        elif w > x // 2:
            w -= 1
        elif w == x // 2 and h == y // 2:
            color = white
        if h < y // 2:
            h += 1
        elif h > y // 2:
            h -= 1
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            # if event.key == pg.K_UP and event.key == pg.K_RIGHT:
            #     motion = 'upright'
            # elif event.key == pg.K_LEFT:
            #     motion = 'left'
            # elif event.key == pg.K_RIGHT:
            #     motion = 'right'
            # elif event.key == pg.K_UP:
            #     motion = 'up'
            # elif event.key == pg.K_DOWN:
            #     motion = 'down'
            if event.key == pg.K_1:
                color = red
            elif event.key == pg.K_2:
                color = green
            elif event.key == pg.K_3:
                color = blue
            elif event.key == pg.K_q:
                fig = 'rect'
            elif event.key == pg.K_w:
                fig = 'circle'
            elif event.key == pg.K_e:
                fig = 'triangle'
            elif event.key == pg.K_DELETE:
                wind.fill(black)
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
                motion = 'stop'
        if event.type == pg.QUIT:
            exit()
    clock.tick(fps)