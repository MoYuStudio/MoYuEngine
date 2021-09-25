
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

import system

class MainSystem:

    window_size = [1280,720]
    window_fps = 60

    title = 'Tinyland 弹丸之地'

    screen = pygame.display.set_mode(window_size,pygame.RESIZABLE)
    screen_title = pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    def __init__(self): 

        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        pygame.display.flip()

    def gameloop(self):

        while True:
            self.screen.fill((0,255,0))
            # system.WindowsSystem.menu_main_surface()

            assets = system.AssetsSystem()
            assets.tileland()

            self.screen.blit(C.assets_tileland[0], (0, 0))

            #print(C.assets_tileland)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == VIDEORESIZE:
                    self.window_size = event.dict['size']
                    print(self.window_size)

            pygame.display.update()
            self.clock.tick(self.window_fps)

if __name__ == "__main__":

    main_game = MainSystem()
    main_game.gameloop()