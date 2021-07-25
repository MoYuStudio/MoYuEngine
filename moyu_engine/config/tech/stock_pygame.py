import pygame
import random
import time

pygame.init()

MainWindow = pygame.display.set_mode((500, 500))

a = 300

w = 0

h = 250

wOld = 0

hOld = 250

base = -1.2

MainWindow.fill((255, 255, 255))

while a != 0:
    wOld = w
    w += 3

    hOld = h
    hd = random.randint(-15, 15)
    h += hd + base

    pygame.draw.line(MainWindow, (0, 0, 0), (wOld, hOld), (w, h), 1)

    pygame.display.update()

    a -= 1

    time.sleep(0.1)

else:
    input()
