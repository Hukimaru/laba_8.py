import pygame as pg
import sys
from pygame.draw import *

clock = pg.time.Clock()
frames_per_second = 144

pg.display.init()
screen = pg.display.set_mode((1000, 1000)) # размеры экрана задаем
screen.fill((100, 100, 100))

#кругляш
circ_kor = (500, 500)
circ_r = 300
circle(screen, (200, 200, 0), circ_kor, circ_r, 0)
circle(screen, (0, 0, 0), circ_kor, circ_r, 5)

#брови
line(screen, (0, 0, 0), (circ_kor[0] + 50, circ_kor[1] - 130), (circ_kor[0] + 400, circ_kor[1] - 250), 55)#левая
line(screen, (0, 0, 0), (circ_kor[0] - 50, circ_kor[1] - 120), (circ_kor[0] - 350, circ_kor[1] - 300), 55)#правая

#глаза
leye = (circ_kor[0] - 100, circ_kor[1] - 50)#центр левого
circle(screen, (255, 0, 0), leye, 40, 0)#левый красный
circle(screen, (0, 0, 0), leye, 40, 5)#левый обвод
circle(screen, (0, 0, 0), leye, 20, 0)#левый зрачок

reye = (circ_kor[0] + 100, circ_kor[1] - 50)#центр левого
circle(screen, (255, 0, 0), reye, 40, 0)#левый красный
circle(screen, (0, 0, 0), reye, 40, 5)#левый обвод
circle(screen, (0, 0, 0), reye, 20, 0)#левый зрачок

#рот
rect(screen, (0, 0, 0), (circ_kor[0] - 150, circ_kor[1] + 30, 300, 50), 0)
pg.display.update()
while True:
    clock.tick(frames_per_second)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


#pg.display.flip()
