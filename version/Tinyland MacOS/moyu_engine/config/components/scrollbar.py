
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C

# scrollbar_h button_pos >>> button_x,button_y+move
# scrollbar_w button_pos >>> button_x+move,button_y

def scrollbar_h_surface(surface):

    if C.scrollbar_move <= 0:
        C.scrollbar_move = 0
    if C.scrollbar_move >= C.scrollbar_line_size[1]-C.scrollbar_button_size[1]:
        C.scrollbar_move = C.scrollbar_line_size[1]-C.scrollbar_button_size[1]

    pygame.draw.rect(surface, C.scrollbar_line_color,(C.scrollbar_line_pos,C.scrollbar_line_size), width=0)
    pygame.draw.rect(surface, C.scrollbar_button_color,(C.scrollbar_button_pos[0],C.scrollbar_button_pos[1]+C.scrollbar_move,C.scrollbar_button_size[0],C.scrollbar_button_size[1]), width=0)

def scrollbar_h_event_MOUSEMOTION():

    if C.scrollbar_moveable == True:
        C.scrollbar_move = (C.mouse_pos_y - C.mouse_down_pos_y)

def scrollbar_h_event_MOUSEBUTTONDOWN():

    if C.scrollbar_button_pos[0] <= C.mouse_down_pos_x <= C.scrollbar_button_pos[0] + C.scrollbar_button_size[0] and C.scrollbar_button_pos[1]+C.scrollbar_move <= C.mouse_down_pos_y <= C.scrollbar_button_pos[1]+C.scrollbar_move + C.scrollbar_button_size[1]:
        C.scrollbar_moveable = True
    else:
        C.scrollbar_moveable = False

def scrollbar_h_event_MOUSEBUTTONUP():

    C.scrollbar_moveable = False

def scrollbar_h_event_MOUSEWHEEL(event):

    mousewheel = event.y

    C.scrollbar_move += mousewheel


