import pygame
import math as m
import time
from objects import *
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

Len_x = 1000
Len_y = 1000

screen = pygame.display.set_mode((Len_x, Len_y))

gun = GUN(Len_x, Len_y, screen)
targ = TARG(Len_x, Len_y)

snar = SNAR(gun, screen)
snar.polet(gun)
gun.new_p()
targ.target(screen, Len_y, Len_x)
pygame.display.update()

clock = pygame.time.Clock()
t3 = 0
finish = False
t1 = time.time()
puly = []
targets = []
nazhatie = False
targets.append(targ)
schot = 0
while not finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.MOUSEMOTION:
            (x, y) = event.pos
            gun.phi = m.atan((-y + Len_y - 100)/(x - 100))
            gun.phi = m.acos((x - 100)/(rast(x, y, 100, Len_y - 100)))
            gun.new_p()
        if event.type == pygame.MOUSEBUTTONDOWN:
            t1 = time.time()  # начало отсчета времени нажатия
            nazhatie = True
        if event.type == pygame.MOUSEBUTTONUP:
            t2 = time.time()  # конец отсчета времени нажатия
            gun.t = t2 - t1
            t1 = 0
            t3 = t2 #отсчет времени жизни снаряда
            puly.append(SNAR(gun, screen))
            nazhatie = False

    if nazhatie:
        gun.t = time.time() - t1
            #snar = SNAR(gun, screen)
    '''if t1:
        gun.t = time.time() - t1
    if snar.l[1] >= Len_y - snar.r - 100:
        snar.l =(snar.l[0] ,- snar.l[1] + 2 * (Len_y - 100 - snar.r))
        snar.dy = -snar.dy * 0.4
        snar.dx = snar.dx * 0.8
        snar.udar += 1
        if snar.udar >= 3:
            circle(screen, BLACK, snar.l, snar.r)
    if time.time() - t3 > 3 and t3:
        circle(screen, BLACK, snar.l, snar.r)
    if (snar.dy ** 2 + snar.dx ** 2) <= 10:
        screen.fill(BLACK)
        gun.new_p()

        targ.target()
    '''
    for snaryad in puly:
        snaryad.polet(gun)
        snaryad.life += 1
        if snaryad.life >= FPS*5:
            circle(screen, BLACK, snaryad.l, snaryad.r)
            puly.remove(snaryad)
        for target_1 in targets:
            if kasanie(snaryad, target_1):
                circle(screen, BLACK, snaryad.l, snaryad.r)
                circle(screen, BLACK, target_1.l, target_1.r)
                schot += 1
                print(schot)
                targets.remove(target_1)
                puly.remove(snaryad)
                targets.append(TARG(Len_x, Len_y))
    for target_1 in targets:
        target_1.target(screen, Len_y, Len_x)

    gun.new_p()
    pygame.display.update()

pygame.quit()
