
import sys

import pygame
import pygame.locals as pglocals

import config

import system.setting as S
import system.assets as A

class GuiSurface:
    def __init__(self,alpha_color=(0,0,0,0)):
        self.surface_size = S.WINDOW_SIZE
        self.surface = pygame.Surface(S.WINDOW_SIZE,flags=pglocals.SRCALPHA).convert_alpha()
        self.surface.fill(alpha_color)
    
    def update(self,interval):
        self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
        button_text = A.font1.render('新游戏', True, (255, 255, 255))
        self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
        self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
        button_text = A.font1.render('继续', True, (255, 255, 255))
        self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
        self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
        button_text = A.font1.render('设置', True, (255, 255, 255))
        self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
        self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
        button_text = A.font1.render('退出', True, (255, 255, 255))
        self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
        self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
        button_text = A.font1.render('关于', True, (255, 255, 255))
        self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))
        return self.surface

    def accept(self,evt):
        button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
        button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
        button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
        button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
        button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

        if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
            S.button_sound.play()

            MENUmain = False
            GAMEmain = True

        if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
            S.button_sound.play()

            MENUmain = False
            GAMEmain = True

        if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
            S.button_sound.play()

        if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
            S.button_sound.play()

            pygame.quit()
            sys.exit()

        if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
            S.button_sound.play()
            return False

'''

def blit():
    suface()

def suface():

    self.surface.fill((0,0,0,0))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
    button_text = A.font1.render('新游戏', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
    button_text = A.font1.render('继续', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
    button_text = A.font1.render('设置', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
    button_text = A.font1.render('退出', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
    button_text = A.font1.render('关于', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

    S.SCREEN.blit(self.surface, (0, 0))

def event():

    button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
    button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
    button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
    button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
    button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

    if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
        S.button_sound.play()

        moyu_engine.config.components.tilemap_manager.tilemap_builder()

        MENUmain = False
        GAMEmain = True

    if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
        S.button_sound.play()

        moyu_engine.config.components.read_data.read_tilemap()

        MENUmain = False
        GAMEmain = True

    if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
        S.button_sound.play()

    if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
        S.button_sound.play()

        pygame.quit()
        sys.exit()

    if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
        S.button_sound.play()
'''
