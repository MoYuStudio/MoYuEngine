
import pygame

import config

import system.setting as S
import system.assets as A

def blit():
    S.SCREEN.fill((0,0,0,0))
    S.SCREEN.blit(A.menu_backgroundFin, (0, 0))