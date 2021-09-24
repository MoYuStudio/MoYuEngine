
import sys
import pygame
from pygame.locals import *

class WindowsSystem():
    # __slots__ = []

    window_size = [1280,720]
    window_fps = 60

    clock = pygame.time.Clock()
    interval = clock.get_time()

    background_surface_size = window_size
    info_surface_size       = window_size
    gui_surface_size        = window_size
    popup_surface_size      = window_size
    transition_surface_size = window_size
    
    # @ classmethod
    # @ staticmethod
    # def __init__(self):
    #     self.background_surface = background_surface

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((self.window_size),pygame.RESIZABLE)

        pygame.display.set_caption('Tinyland 弹丸之地')
        # pygame.display.set_icon(A.tl6)
        pygame.display.flip()

        self.background_surface = pygame.Surface(self.background_surface_size).convert_alpha()
        self.info_surface       = pygame.Surface(self.info_surface_size).convert_alpha()
        self.gui_surface        = pygame.Surface(self.gui_surface_size).convert_alpha()
        self.popup_surface      = pygame.Surface(self.popup_surface_size).convert_alpha()
        self.transition_surface = pygame.Surface(self.transition_surface_size).convert_alpha()

    def background(self,background_surface_add): 
        self.background_surface.fill((0,0,0,0))
        self.background_surface.blit(background_surface_add, (0, 0))

    def info(self): 
        self.info_surface.fill((0,0,0,0))

    def gui(self): 
        self.gui_surface.fill((0,0,0,0))

    def popup(self): 
        self.popup_surface.fill((0,0,0,0))

    def transition(self): 
        self.transition_surface.fill((0,0,0,0))

    def window_blit(self):
        
        self.background()
        self.info()
        self.gui()
        self.popup()
        self.transition()

        background_surfaceFin = pygame.transform.scale(self.background_surface, self.window_size)
        info_surfaceFin       = pygame.transform.scale(self.info_surface, self.window_size)
        gui_surfaceFin        = pygame.transform.scale(self.gui_surface, self.window_size)
        popup_surfaceFin      = pygame.transform.scale(self.popup_surface, self.window_size)
        transition_surfaceFin = pygame.transform.scale(self.transition_surface, self.window_size)

        self.screen.blit(background_surfaceFin, (0, 0))
        self.screen.blit(info_surfaceFin, (0,0))
        self.screen.blit(gui_surfaceFin, (0, 0))
        self.screen.blit(popup_surfaceFin, (0, 0))
        self.screen.blit(transition_surfaceFin, (0, 0))

        pygame.display.update()
        self.clock.tick(self.window_fps)

    def window_event(self):
        for event in pygame.event.get(): 
            if  event.type == QUIT: 
                    pygame.quit()
                    sys.exit()

            if event.type == VIDEORESIZE:
                    self.windowsize = event.dict

if __name__ == "__main__":

    window_system = WindowsSystem()
    window_system.window_blit()
    window_system.window_event()