
import pygame
from pygame.locals import *

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.font as F

import moyu_engine.config.components.fade_black

def blit(): 

    background()
    info()
    gui()
    popup()
    transition()

    background_surfaceFin = pygame.transform.scale(background_surface, C.WINDOW_SIZE)
    info_surfaceFin       = pygame.transform.scale(info_surface, C.WINDOW_SIZE)
    gui_surfaceFin        = pygame.transform.scale(gui_surface, C.WINDOW_SIZE)
    popup_surfaceFin      = pygame.transform.scale(popup_surface, C.WINDOW_SIZE)
    transition_surfaceFin = pygame.transform.scale(transition_surface, C.WINDOW_SIZE)

    C.SCREEN.blit(background_surfaceFin, (0, 0))
    C.SCREEN.blit(info_surfaceFin, (0,0))
    C.SCREEN.blit(gui_surfaceFin, (0, 0))
    C.SCREEN.blit(popup_surfaceFin, (0, 0))
    C.SCREEN.blit(transition_surfaceFin, (0, 0))

def background(): 
    background_surface.fill((0,0,0,0))

    background_surface.blit(G.menu_backgroundFin, (0,0))

def info(): 
    info_surface.fill((0,0,0,0))
    pass

def gui(): 
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

def popup(): 
    popup_surface.fill((0,0,0,0))
    pass

def transition(): 
    transition_surface.fill((0,0,0,0))
    pass

background_surface_size = C.WINDOW_SIZE
background_surface      = pygame.Surface(background_surface_size).convert_alpha()
info_surface_size       = C.WINDOW_SIZE
info_surface            = pygame.Surface(info_surface_size).convert_alpha()
gui_surface_size        = C.WINDOW_SIZE
gui_surface             = pygame.Surface(gui_surface_size).convert_alpha()
popup_surface_size      = C.WINDOW_SIZE
popup_surface           = pygame.Surface(popup_surface_size).convert_alpha()
transition_surface_size = C.WINDOW_SIZE
transition_surface      = pygame.Surface(transition_surface_size).convert_alpha()
