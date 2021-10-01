
import os
import sys
import threading
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

        system.ThreadSystem.thread0(system.AssetsSystem.loader())
        

    def gameloop(self):

        system.TilemapSystem.tilemap_builder()

        while True:

            system.ThreadSystem.thread1(system.MoveSystem.move())
            system.ThreadSystem.thread1(system.MoveSystem.zoom())

            C.screen.fill((255,55,55,0))

            if C.window['page_switch']['menu_main_page'] == True:

                system.WindowsSystem.menu_main_surface()

            if C.window['page_switch']['game_main_page'] == True:

                system.WindowsSystem.game_main_surface()
            
            pygame.display.update()
            self.clock.tick(C.window['fps'])

if __name__ == "__main__":

    main_game = MainSystem()
    main_game.gameloop()