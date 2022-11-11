import pygame
from pygame.draw import *
from random import randint
pygame.init()

#класс шариков
class shar:
    def new_shar(self, screen, color, l, r):
        circle(screen, color, l, r)

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
'''
shar1 = shar()
l = (100, 100)
shar1.new_shar(screen, RED, l, 40)
'''
rect(screen, RED, (0, 0, 300, 300), 2)
pygame.display.update()

