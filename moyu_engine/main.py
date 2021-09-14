
# from moyu_engine.config.surface import background
import pygame
from pygame.locals import *

import config.system.setting as S

# import config.surface.background
# import config.event.event

from config.event import MainEvent
from config.surface import BackgroundSurface

class MainGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(S.WINDOW_SIZE)
        background = BackgroundSurface()
        self.event = MainEvent(initial_stack=[background])

        pygame.display.set_caption('Tinyland 弹丸之地')
        #pygame.display.set_icon(G.tl16)
        pygame.display.flip()

    def gameloop(self): 
        # declare clock here
        clock = pygame.time.Clock()
        while True:
            clock.tick(S.WINDOW_FPS)
            interval = clock.get_time()
            # print(interval)
            self.event.distribute()
            self.event.update_all(interval,self.screen)

            pygame.display.update()

if __name__=="__main__":
    main_game = MainGame()
    main_game.gameloop()