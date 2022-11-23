import pygame
import math as m
import time
from pygame.draw import *
from random import randint


class SNAR:
    def __init__(self, gun, screen):
        self.r = 40  # радиус снаряда
        self.V = gun.t * 50  # зависимость скорости от времени нажатия мыши. gun.t - время пока кнопка зажата
        self.color = YELLOW
        gun.t = 0
        self.l = ((gun.D[0] + gun.C[0]) // 2, (gun.D[1] + gun.C[1]) // 2)
        self.dy = -self.V * m.sin(gun.phi)
        self.dx = self.V * m.cos(gun.phi)
        self.life = 0
        self.screen = screen


    def polet(self, gun):
        '''
        Рисует новый кадр снаряда и считает новые скорости и координаты.
        '''
        circle(self.screen, BLACK, self.l, self.r)
        if self.l[0] >= gun.Len_x - self.r or self.l[0] <= self.r:
            self.dx = -1 * self.dx
        if self.l[1] >= gun.Len_y - self.r or self.l[0] <= self.r :
            self.dy = -1 * self.dy
        self.l = (self.l[0] + self.dx, self.l[1] + self.dy)
        circle(self.screen, GREEN, self.l, self.r)
        self.dy = (self.dy + 1) * 0.99
        self.dx = self.dx * 0.97

class GUN:
    def __init__(self, Len_x, Len_y, screen):
        '''Создает пушку
        Len_x - ширина экрана
        Len_y - высота экрана
        '''
        self.t = 100
        self.phi = m.pi / 4
        self.Sh = 25*(1 - 0.4/self.t)  # ширина пушки
        self.L = 200*(1 + 0.5/self.t)  # длина пушки
        self.color = GRAY
        self.A = (100 - self.Sh * m.sin(self.phi), Len_y - 100 - self.Sh * m.cos(self.phi))
        '''self.A = ((self.L**2 + self.Sh**2)**0.5 * m.cos(self.phi + m.atan(0.5*self.Sh/self.L)), (self.L**2 + self.Sh**2)**0.5 * m.sin(self.phi + m.atan(0.5*self.Sh/self.L)))
        ''' # другой подсчет координат
        self.B = (100 + self.Sh * m.sin(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 - self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  Len_y - 100 + self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))
        self.screen = screen
        self.Len_x = Len_x
        self.Len_y = Len_y

    def new_p(self):
        '''рисует пушку в зависимости от координат мыши'''
        polygon(self.screen, BLACK, (self.A, self.B, self.D, self.C))
        self.L = 100 + self.t * 30
        self.A = (100 - self.Sh * m.sin(self.phi), self.Len_y - 100 - self.Sh * m.cos(self.phi))
        self.B = (100 + self.Sh * m.sin(self.phi), self.Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  self.Len_y - 100 - self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L * m.cos(self.phi),
                  self.Len_y - 100 + self.Sh * m.cos(self.phi) - self.L * m.sin(self.phi))

        polygon(self.screen, GRAY, (self.A, self.B, self.D, self.C))

    '''
    def vers(self):
        self.A = (100 - self.Sh*m.sin(self.phi), Len_y - 100 - self.Sh*m.cos(self.phi))
        self.B = (100 + self.Sh * m.sin(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi))
        self.C = (100 - self.Sh * m.sin(self.phi) + self.L*m.cos(self.phi), Len_y - 100 - self.Sh * m.cos(self.phi) - self.L*m.sin(self.phi))
        self.D = (100 + self.Sh * m.sin(self.phi) + self.L*m.cos(self.phi), Len_y - 100 + self.Sh * m.cos(self.phi) - self.L*m.sin(self.phi))
    '''
def kasanie(targ, snar):
    '''проверяет коснулся ли шарик мишени'''
    if rast(targ.l[0], targ.l[1], snar.l[0], snar.l[1]) <= targ.r + snar.r:
        return True
    else:
        return False

class TARG:
    """класс мишени. Пока только создает мишень и русует ее"""
    def __init__(self, Len_x, Len_y):
        self.l = (Len_x - 200, 200)
        self.r = 50
        self.color = RED
        self.dx = randint(-10, 10)
        self.dy = randint(-10, 10)

    def target(self, screen, Len_y, Len_x):
        circle(screen, BLACK, self.l, self.r)
        self.l = (self.l[0] + self.dx, self.l[1] + self.dy)

        if self.l[0] >= Len_x - self.r or self.l[0] <= self.r:
            self.dx = -1 * self.dx
        if self.l[1] >= Len_y - self.r or self.l[1] <= self.r :
            self.dy = -1 * self.dy
        self.l = (self.l[0] + self.dx, self.l[1] + self.dy)

        circle(screen, self.color, self.l, self.r)
        #self.dy = self.dy - 1
        #self.dx *= 0.98

def rast(x, y, x1, y1): # расстояние мерить
    return ((x - x1)**2 + (y - y1)**2)**0.5

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]