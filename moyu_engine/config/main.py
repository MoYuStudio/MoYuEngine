
import sys
import pygame
from pygame.locals import *

import assets.graphics as G

class MainGame      : 
    def __init__(self): 

        pygame.init()
        pygame.mixer.init()

        self.window_fps   = 60
        self.window_level = 60
        self.window_size  = [16*self.window_level,9*self.window_level]

        self.window_title = 'Tinyland 弹丸之地'

        self.screen = pygame.display.set_mode((self.window_size),pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.window_title)
        pygame.display.set_icon(G.tl6)
        pygame.display.flip()

    def gameloop(self): 

        while True: 

            self.screen.fill((0,0,0,0))

            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()

            self.clock.tick(self.window_fps)

if __name__ == "__main__":

    main_game = MainGame()
    main_game.gameloop()