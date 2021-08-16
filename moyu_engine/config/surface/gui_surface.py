
import sys
import pygame
from pygame.locals import *

import constants as C
import graphics as G
import font as F

import components.scrollbar

def graphics(): 
    components.scrollbar.scrollbar_h_display(C.gui_surface,(255,0,0),(10,10),(3,30),(0,255,0),(10,10),(5,3),line_width=0,button_width=0)