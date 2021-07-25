
import sys
import pygame
from pygame.locals import *

mainwindow = pygame.display.set_mode((600,600))
window_title = pygame.display.set_caption('test')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

mouse_oldpos_x,mouse_oldpos_y = 0,0
mouse_display = False

mouse_clicker_on = True
mouse_clicker_off = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            mouse_pos_x,mouse_pos_y = event.pos

            mouse_nowpos_x,mouse_nowpos_y = mouse_pos_x,mouse_pos_y

            if mouse_display == False:

                mainwindow.fill((0,0,0))

                pygame.display.update()

            if mouse_display == True:

                mainwindow.fill((0,0,0))

                pygame.draw.line(mainwindow, (255, 255, 255), (mouse_oldpos_x,mouse_oldpos_y),(mouse_pos_x,mouse_pos_y),3)
                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos_x,mouse_pos_y = event.pos

            if mouse_clicker_on == False:
                mouse_clicker_off = True

            if mouse_clicker_on == True:

                mouse_oldpos_x,mouse_oldpos_y = mouse_pos_x,mouse_pos_y

                mouse_display = True
                mouse_clicker_on = False
                print('off')

            if mouse_clicker_off == True:

                mouse_oldpos_x,mouse_oldpos_y = 0,0

                mouse_display = False
                mouse_clicker_off = False

                mouse_clicker_on = True
                print('on')
