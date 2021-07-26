
import sys
import pygame
from pygame.locals import *

mainwindow = pygame.display.set_mode((600,600))
window_title = pygame.display.set_caption('test')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

button_x,button_y = 172, 100
button_w,button_h = 25, 50

moveable = False
move = 0

mouse_x, mouse_y = 0,0
mouse_pos_x,mouse_pos_y = 0,0

while True:

    mainwindow.fill((0,0,0))

    pygame.draw.rect(mainwindow, (255, 255, 255),(180, 100, 10, 350), width=0)
    pygame.draw.rect(mainwindow, (161, 136, 127),(button_x,button_y+move,button_w,button_h), width=0)
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            mouse_pos_x,mouse_pos_y = event.pos
            if moveable == True:
                move = mouse_pos_y - mouse_y

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if button_x <= mouse_x <= button_x + button_w and button_y+move <= mouse_y <= button_y+move + button_h:
                print('button be clicked')
                moveable = True
            else:
                moveable = False

        if event.type == pygame.MOUSEBUTTONUP:

            moveable = False



