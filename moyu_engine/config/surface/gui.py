
import pygame

import config

import system.setting as S
import system.assets as A

gui_surface_size        = S.WINDOW_SIZE
gui_surface             = pygame.Surface(gui_surface_size).convert_alpha()

def blit():
    MENUmain_suface()

def MENUmain_suface():

    gui_surface.fill((0,0,0,0))
    gui_surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
    button_text = A.font1.render('新游戏', True, (255, 255, 255))
    gui_surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
    gui_surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
    button_text = A.font1.render('继续', True, (255, 255, 255))
    gui_surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
    gui_surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
    button_text = A.font1.render('设置', True, (255, 255, 255))
    gui_surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
    gui_surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
    button_text = A.font1.render('退出', True, (255, 255, 255))
    gui_surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
    gui_surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
    button_text = A.font1.render('关于', True, (255, 255, 255))
    gui_surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

    S.SCREEN.blit(gui_surface, (0, 0))
