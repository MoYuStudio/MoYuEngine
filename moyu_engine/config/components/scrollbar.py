
import pygame
from pygame.locals import *

import constants as C

# scrollbar_h button_pos >>> button_x,button_y+move
# scrollbar_w button_pos >>> button_x+move,button_y

def scrollbar_h_display(surface,line_color,line_pos,line_size,button_color,button_pos,button_size,line_width=0,button_width=0):
    pygame.draw.rect(surface, (line_color),(line_pos,line_size), width=line_width)
    pygame.draw.rect(surface, (button_color),(button_pos,button_size), width=button_width)

def scrollbar_h_input(button_pos,button_size):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse_pos_x,mouse_pos_y = event.pos

        if moveable == True:
            move = mouse_pos_y - mouse_y

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if button_pos[0] <= mouse_x <= button_pos[0] + button_size[0] and button_pos[1]+move <= mouse_y <= button_pos[1]+move + button_size[1]:
                print('scrollbar_button be clicked')
                moveable = True
            else:
                moveable = False

        if event.type == pygame.MOUSEBUTTONUP:

            moveable = False
