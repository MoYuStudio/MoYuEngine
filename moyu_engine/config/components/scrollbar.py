
import pygame
from pygame.locals import *

import constants as C

# scrollbar_h button_pos >>> button_x,button_y+move
# scrollbar_w button_pos >>> button_x+move,button_y

def scrollbar_h_surface(surface,scrollbar_line_color,scrollbar_line_pos,scrollbar_line_size,scrollbar_button_color,scrollbar_button_pos,scrollbar_button_size,scrollbar_move):

    if scrollbar_move <= 0:
        scrollbar_move = 0
    if scrollbar_move >= scrollbar_line_size[1]-scrollbar_button_size[1]:
        scrollbar_move = scrollbar_line_size[1]-scrollbar_button_size[1]

    pygame.draw.rect(surface, scrollbar_line_color,(scrollbar_line_pos,scrollbar_line_size), width=0)
    pygame.draw.rect(surface, scrollbar_button_color,(scrollbar_button_pos[0],scrollbar_button_pos[1]+scrollbar_move,scrollbar_button_size[0],scrollbar_button_size[1]), width=0)

    return scrollbar_move,scrollbar_line_size,scrollbar_button_size

def scrollbar_h_event_MOUSEMOTION(scrollbar_move,scrollbar_moveable):

    if scrollbar_moveable == True:
        scrollbar_move = C.mouse_pos_y - C.mouse_down_pos_y

    return scrollbar_move

def scrollbar_h_event_MOUSEBUTTONDOWN(scrollbar_button_pos,scrollbar_button_size,scrollbar_move,scrollbar_moveable):

    if scrollbar_button_pos[0] <= C.mouse_down_pos_x <= scrollbar_button_pos[0] + scrollbar_button_size[0] and scrollbar_button_pos[1]+scrollbar_move <= C.mouse_down_pos_y <= scrollbar_button_pos[1]+scrollbar_move + scrollbar_button_size[1]:
        scrollbar_moveable = True
        print('233333')
    else:
        scrollbar_moveable = False

    return scrollbar_moveable

def scrollbar_h_event_MOUSEBUTTONUP():

    scrollbar_moveable = False

def scrollbar_h_event_MOUSEWHEEL():

    mousewheel = event.y

    scrollbar_move += mousewheel

