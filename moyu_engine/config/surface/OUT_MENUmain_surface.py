
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.fade_black

def update():

    '''
    fade = pygame.Surface((C.WINDOW_SIZE))
    fade.fill((0,0,0))

    C.SCREEN.blit(fade, (0,0))
    '''


    MENUgraphics()

    MENUmain_surfaceFin = pygame.transform.scale(C.MENUmain_surface,C.WINDOW_SIZE)

    #MENUmain_surfaceFin.set_alpha(100)
    
    C.SCREEN.blit(MENUmain_surfaceFin, (0, 0))

    moyu_engine.config.components.fade_black.fade_black_surface()
    if C.window_switch == True and C.buttonStartGame == True:
        C.MENUmain = False
        C.GAMEmain = True

        C.window_switch = False
        C.buttonStartGame = False
    moyu_engine.config.components.fade_black.fade_black_blit()

def MENUgraphics():

    C.MENUmain_surface_size = [16*C.MENUmain_surface_level,9*C.MENUmain_surface_level]
    C.MENUmain_surface = pygame.Surface(C.MENUmain_surface_size)

    C.MENUmain_surface.blit(G.menu_backgroundFin, (0,0))

    C.MENUmain_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*5 - 10*5))
    startbutton_text = F.font1.render('新游戏', True, (255, 255, 255))
    C.MENUmain_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*5 - 10*5))

    C.MENUmain_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*4 - 10*4))
    startbutton_text = F.font1.render('继续', True, (255, 255, 255))
    C.MENUmain_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*4 - 10*4))

    C.MENUmain_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*3 - 10*3))
    startbutton_text = F.font1.render('设置', True, (255, 255, 255))
    C.MENUmain_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*3 - 10*3))

    C.MENUmain_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*2 - 10*2))
    startbutton_text = F.font1.render('退出', True, (255, 255, 255))
    C.MENUmain_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*2 - 10*2))

    C.MENUmain_surface.blit(G.button001_unclickFin, (C.WINDOW_SIZE[0]-64*3*1 - 20, C.WINDOW_SIZE[1]-16*3*1 - 10*1))
    startbutton_text = F.font1.render('关于', True, (255, 255, 255))
    C.MENUmain_surface.blit(startbutton_text,(C.WINDOW_SIZE[0]-64*2.5*1, C.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

def fade_black():

    if C.fade_black == True:
        if C.alpha >= -100 :
            C.alpha -= 10
            C.MENUmain_surface.set_alpha(C.alpha)
        if 0 >= C.alpha >= -100:
            C.fade_black = False
            C.alpha = 255
            C.window_switch = True

            if C.window_switch == True and C.buttonStartGame == True:
                C.MENUmain = False
                C.GAMEmain = True

                C.window_switch = False
                C.buttonStartGame = False

