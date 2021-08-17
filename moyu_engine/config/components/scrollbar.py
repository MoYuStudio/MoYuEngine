
import pygame
from pygame.locals import *

import constants as C

# scrollbar_h button_pos >>> button_x,button_y+move
# scrollbar_w button_pos >>> button_x+move,button_y

def scrollbar_h_display(surface,line_color,line_pos,line_size,button_color,button_pos,button_size,line_width=0,button_width=0):
    pygame.draw.rect(surface, line_color,(line_pos,line_size), width=line_width)
    pygame.draw.rect(surface, button_color,(button_pos,button_size), width=button_width)

def scrollbar_h_input():
    if C.scrollbar_moveable == True:
        C.scrollbar_move = C.mouse_pos_y - C.mouse_down_pos_y

def scrollbar_h_MOUSEBUTTONDOWN(button_pos,button_size):

    if button_pos[0] <= C.mouse_down_pos_x <= button_pos[0] + button_size[0] and button_pos[1]+C.scrollbar_move <= C.mouse_down_pos_y <= button_pos[1]+C.scrollbar_move + button_size[1]:
        print('scrollbar_button be clicked')
        C.scrollbar_moveable = True
    else:
        C.scrollbar_moveable = False

def scrollbar_h_MOUSEBUTTONUP():

    C.scrollbar_moveable = False

