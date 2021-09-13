
import pygame
from pygame.locals import *

import config.system.setting as S

import config.surface.background

import config.event.event

def run(): 
    init()
    gameloop()

def init(): 

    pygame.init()
    pygame.mixer.init()

    S.SCREEN = pygame.display.set_mode(S.WINDOW_SIZE)
    SCREEN_TITLE = pygame.display.set_caption('Tinyland 弹丸之地')

    #pygame.display.set_icon(G.tl16)
    
    pygame.display.flip()

    return S.SCREEN

def gameloop(): 

    while True:

        config.surface.background.blit()

        config.event.event.event()

        pygame.display.update()
        CLOCK = pygame.time.Clock()
        CLOCK.tick(S.WINDOW_FPS)

run()