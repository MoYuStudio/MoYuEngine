
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

screen = pygame.display.set_mode([320,180])

class Surface:
    def __init__(self,surface_data = {
                                        'blit_window':'',
                                        'blit_surface':'',
                                        'surface_size':[1920,1080],
                                        'background_size':[1920,1080],
                                        'info_size':[1920,1080],
                                        'gui_size':[1920,1080],
                                        'popup_size':[1920,1080],
                                        'transition_size':[1920,1080],
                                        'window_size':[1920,1080],
                                    }):
        self.surface_data = surface_data

        self.background_surface = pygame.Surface(self.surface_data['background_size']).convert_alpha()
        self.background_surface.fill((255,55,55,0))
        self.info_surface = pygame.Surface(self.surface_data['info_size']).convert_alpha()
        self.info_surface.fill((255,55,55,0))
        self.gui_surface = pygame.Surface(self.surface_data['gui_size']).convert_alpha()
        self.gui_surface.fill((255,55,55,0))
        self.popup_surface = pygame.Surface(self.surface_data['popup_size']).convert_alpha()
        self.popup_surface.fill((255,55,55,0))
        self.transition_surface = pygame.Surface(self.surface_data['transition_size']).convert_alpha()
        self.transition_surface.fill((255,55,55,0))

    def blit(self):

        self.background_surfaceFin = pygame.transform.scale(self.background_surface,self.surface_data['window_size'])
        self.info_surfaceFin = pygame.transform.scale(self.info_surface,self.surface_data['window_size'])
        self.gui_surfaceFin = pygame.transform.scale(self.gui_surface,self.surface_data['window_size'])
        self.popup_surfaceFin = pygame.transform.scale(self.popup_surface,self.surface_data['window_size'])
        self.transition_surfaceFin = pygame.transform.scale(self.transition_surface,self.surface_data['window_size'])

        self.surface_data['blit_surface'].blit(self.background_surfaceFin, (0, 0))
        self.surface_data['blit_surface'].blit(self.info_surface, (0, 0))
        self.surface_data['blit_surface'].blit(self.gui_surface, (0, 0))
        self.surface_data['blit_surface'].blit(self.popup_surface, (0, 0))
        self.surface_data['blit_surface'].blit(self.transition_surface, (0, 0))

        self.surface_data['blit_window'].blit(self.surface_data['blit_surface'], (0, 0))
        
        pygame.display.update()

    def background(self):
        pass
        
    def info(self):
        pass

    def gui(self):
        pass

    def popup(self):
        pass

    def transition(self):
        pass
        
if __name__ == "__main__":
    pass
