
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class MainSystem:
    
    C.screen = pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)
    screen_title = pygame.display.set_caption(C.window['title'])
    clock = pygame.time.Clock()

    def __init__(self): 

        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        pygame.display.flip()

        assets = system.AssetsSystem()
        assets.tileland()

    def gameloop(self):

        while True:
            C.screen.fill((0,255,0))

            C.screen.blit(C.assets['tileland'][1], (0, 0))

            # print(C.assets_tileland)

            system.WindowsSystem.menu_main_surface()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == VIDEORESIZE:
                    C.window['size'] = event.dict['size']
                    print(C.window['size'])

            pygame.display.update()
            self.clock.tick(C.window['fps'])

if __name__ == "__main__":

    main_game = MainSystem()
    main_game.gameloop()