
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class WindowsSystem:

    @ staticmethod
    def menu_main_surface():

        background_surface      = pygame.Surface(C.window['size']).convert_alpha()
        gui_surface             = pygame.Surface(C.window['size']).convert_alpha()

        background_surface.fill((0,0,0,0))
        background_surface.fill((255,0,0))

        gui_surface.fill((0,0,0,0))
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

        menu_main_surface = pygame.Surface(C.window['size']).convert_alpha()

        menu_main_surface.blit(background_surface, (0, 0))
        menu_main_surface.blit(gui_surface, (0, 0))
        
        C.screen.blit(menu_main_surface, (0, 0))