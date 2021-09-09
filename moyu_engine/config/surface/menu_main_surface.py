
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

def update():

    menu_graphics()

    menu_main_surfaceFin = pygame.transform.scale(C.menu_main_surface,C.window_size)
    
    C.screen.blit(menu_main_surfaceFin, (0, 0))

def menu_graphics():
    C.menu_main_surface_size = [16*C.menu_main_surface_level,9*C.menu_main_surface_level]
    C.menu_main_surface = pygame.Surface(C.menu_main_surface_size)

    C.menu_main_surface.fill((255,255,255))

    C.menu_main_surface.blit(G.menu_backgroundFin, (0,0))

    C.menu_main_surface.blit(G.buttonFin, (C.window_size[0]-64*3*1 - 20, C.window_size[1]-16*3*5 - 10*5))
    startbutton_text = F.font1.render('新游戏', True, (255, 255, 255))
    C.menu_main_surface.blit(startbutton_text,(C.window_size[0]-64*2.5*1, C.window_size[1]-16*2.87*5 - 10*5))

    C.menu_main_surface.blit(G.buttonFin, (C.window_size[0]-64*3*1 - 20, C.window_size[1]-16*3*4 - 10*4))
    startbutton_text = F.font1.render('继续', True, (255, 255, 255))
    C.menu_main_surface.blit(startbutton_text,(C.window_size[0]-64*2.5*1, C.window_size[1]-16*2.87*4 - 10*4))

    C.menu_main_surface.blit(G.buttonFin, (C.window_size[0]-64*3*1 - 20, C.window_size[1]-16*3*3 - 10*3))
    startbutton_text = F.font1.render('设置', True, (255, 255, 255))
    C.menu_main_surface.blit(startbutton_text,(C.window_size[0]-64*2.5*1, C.window_size[1]-16*2.87*3 - 10*3))

    C.menu_main_surface.blit(G.buttonFin, (C.window_size[0]-64*3*1 - 20, C.window_size[1]-16*3*2 - 10*2))
    startbutton_text = F.font1.render('退出', True, (255, 255, 255))
    C.menu_main_surface.blit(startbutton_text,(C.window_size[0]-64*2.5*1, C.window_size[1]-16*2.87*2 - 10*2))

    C.menu_main_surface.blit(G.buttonFin, (C.window_size[0]-64*3*1 - 20, C.window_size[1]-16*3*1 - 10*1))
    startbutton_text = F.font1.render('关于', True, (255, 255, 255))
    C.menu_main_surface.blit(startbutton_text,(C.window_size[0]-64*2.5*1, C.window_size[1]-16*2.87*1 - 10*1))

