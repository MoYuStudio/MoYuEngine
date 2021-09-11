
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.fade_black

def blit():
    background_surface()
    info_surface()
    gui_surface()
    popup_surface()
    transition_surface()

def background_surface():
    background_surface_size = C.WINDOW_SIZE
    background_surface = pygame.Surface(background_surface_size)
    background_surface.blit(G.menu_backgroundFin, (0,0))

    C.SCREEN.blit(background_surface, (0, 0))

def info_surface():
    pass

def gui_surface():
    gui_surface_size = C.WINDOW_SIZE
    gui_surface = pygame.Surface(gui_surface_size)

    gui_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*5 - 10*5))
    startbutton_text = F.font1.render('新游戏', True, (255, 255, 255))
    gui_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*5 - 10*5))

    gui_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*4 - 10*4))
    startbutton_text = F.font1.render('继续', True, (255, 255, 255))
    gui_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*4 - 10*4))

    gui_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*3 - 10*3))
    startbutton_text = F.font1.render('设置', True, (255, 255, 255))
    gui_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*3 - 10*3))

    gui_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*2 - 10*2))
    startbutton_text = F.font1.render('退出', True, (255, 255, 255))
    gui_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*2 - 10*2))

    gui_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*1 - 10*1))
    startbutton_text = F.font1.render('关于', True, (255, 255, 255))
    gui_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

def popup_surface():
    pass

def transition_surface():
    pass