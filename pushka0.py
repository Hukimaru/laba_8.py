import pygame
import math as m
import time
from pygame.draw import *
from random import randint

pygame.init()


class GUN:
    def __init__(self):
        self.phi = m.pi / 4
        self.Sh = 25  # ширина пушки
        self.L = 200  # длина пушки
        self.color = GRAY
        self.t = 100
        self.A = (100 - self.Sh * m.sin(self.phi), Len_y - 100 - self.Sh * m.cos(self.phi))
        self.B = (100 + self.Sh * m.sin(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 - self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 + self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))

    def new_p(self):  # рисует пушку
        polygon(screen, BLACK, (self.A, self.B, self.D, self.C))
        self.L = 100 + gun.t * 30
        self.A = (100 - self.Sh * m.sin(self.phi), Len_y - 100 - self.Sh * m.cos(self.phi))
        self.B = (100 + self.Sh * m.sin(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 - self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 + self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))

        polygon(screen, GRAY, (self.A, self.B, self.D, self.C))

    '''
    def vers(self):
        self.A = (100 - self.Sh*m.sin(self.phi), Len_y - 100 - self.Sh*m.cos(self.phi))
        self.B = (100 + self.Sh * m.sin(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L*m.cos(self.phi), Len_y - 100 - self.Sh * m.cos(self.phi) - self.L*m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L*m.cos(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi) - self.L*m.sin(self.phi))
    '''

class TARG:
    def __init__(self):
        self.l = (Len_x - 200, Len_y - 200)
        self.r = 50
        self.color = RED

    def target(self):
        circle(screen, self.color, self.l, self.r)

class SNAR:
    def __init__(self, gun):
        self.r = 40  # радиус мишени
        self.V = gun.t * 50  # зависимость скорости от времени нажатия мыши. gun.t - время пока кнопка зажата
        self.color = YELLOW
        gun.t = 0
        self.l = ((gun.D[0] + gun.C[0]) // 2, (gun.D[1] + gun.C[1]) // 2)
        self.dy = -self.V * m.sin(gun.phi)
        self.dx = self.V * m.cos(gun.phi)
        self.life = 0

    def polet(self):
        circle(screen, BLACK, self.l, self.r)
        self.l = (self.l[0] + self.dx, self.l[1] + self.dy)
        circle(screen, GREEN, self.l, self.r)
        self.dy = self.dy + 1
        self.dx = self.dx * 0.97

def rast(x, y, x1, y1):  # расстояние мерить
    return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

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

Len_x = 1200
Len_y = 900

screen = pygame.display.set_mode((Len_x, Len_y))

gun = GUN()
targ = TARG()

snar = SNAR(gun)
snar.polet()
gun.new_p()
targ.target()
pygame.display.update()

clock = pygame.time.Clock()
t3 = 0
finish = False
t1 = time.time()
while not finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.MOUSEMOTION:
            (x, y) = event.pos
            gun.phi = m.atan((-y + Len_y - 100)/(x - 100))
            gun.new_p()
        if event.type == pygame.MOUSEBUTTONDOWN:
            t1 = time.time()  # начало отсчета времени нажатия
        if event.type == pygame.MOUSEBUTTONUP:
            t2 = time.time()  # конец отсчета времени нажатия
            gun.t = t2 - t1
            t1 = 0
            t3 = t2 #отсчет времени жизни снаряда
            snar = SNAR(gun)
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

    snar.polet()

    if snar.l[1] >= Len_y -100

    gun.new_p()
    pygame.display.update()

pygame.quit()
