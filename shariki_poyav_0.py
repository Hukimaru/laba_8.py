import pygame
from pygame.draw import *
from random import randint
pygame.init()

#класс шариков
class shar:
    def __init__(self):
        self.color = COLORS[randint(0, 5)] # цвет шара
        self.r = randint(20, 200) # радиус
        self.l = (randint(self.r, 1200 - self.r), randint(self.r, 900 - self.r)) # координаты центра
        self.delta_x = randint(-200//FPS, 200//FPS) # регулирует скорость движения шарика по х
        self.delta_y = randint(-200//FPS, 200//FPS) # регулирует скорость движения шарика по у
        self.life = 0 # что бы считать, сколько жив шарик
        self.LIFE = randint(0, 10*FPS) #randint(5, 10)#сколько он всего будет жить (шарик)

    def new_shar(self, screen): # показ шара с движением
        circle(screen, BLACK, self.l, self.r)
        self.l = (self.l[0] + self.delta_x, self.l[1] + self.delta_y)
        circle(screen, self.color, self.l, self.r)

def rast(x, y, x1, y1): # расстояние мерить
    return ((x - x1)**2 + (y - y1)**2)**0.5

def kasanie(shar_1): #обеспечивает проверку касания стенок
    if shar_1.l[0] <= shar_1.r or shar_1.l[0] >= 1200 - shar_1.r:
        return True
    elif shar_1.l[1] <= shar_1.r or shar_1.l[1] >= 900 - shar_1.r:
        return True
    else:
        return False

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#всего будет 4 независимых шара
shar1 = shar() # шар 1
shar1.new_shar(screen)
shar2 = shar() # шар 2
shar2.new_shar(screen)
shar3 = shar() # шар 3
shar3.new_shar(screen)
shar4 = shar() # шар 4
shar4.new_shar(screen)
BALLS = [shar1, shar2, shar3, shar4] # массив имеющихся шаров

pygame.display.update()

clock = pygame.time.Clock()
finished = False

goals = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            for i in range (len(BALLS)):
                if rast(x, y, BALLS[i].l[0], BALLS[i].l[1]) <= BALLS[i].r:
                    circle(screen, BLACK, BALLS[i].l, BALLS[i].r)
                    BALLS[i] = shar()
                    goals += 1
                    print(goals)
    for ball in BALLS: # считает сколько жил шарик
        ball.life += 1

        #elif event.typr == pygame.MOUSEBUTTONDOWN:
        #    if event.button == 1:

    #screen.fill(BLACK) #чтобы не было следа от шарика

    for ball in BALLS:
        ball.new_shar(screen)
        if kasanie(ball):
            if ball.l[0] >= 1200 - ball.r:
                ball.delta_x = randint(-200//FPS, 0)
            if ball.l[0] <= ball.r:
                ball.delta_x = randint(0, 200//FPS)
            if ball.l[1] >= 900 - ball.r:
                ball.delta_y = randint(-200//FPS, 0)
            if ball.l[1] <= ball.r:
                ball.delta_y = randint(0, 200//FPS)
        pygame.display.update()

    for i in range(len(BALLS)):
        if BALLS[i].life == BALLS[i].LIFE:
            circle(screen, BLACK, BALLS[i].l, BALLS[i].r)
            BALLS[i] = shar()



pygame.quit()
