
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png')#.convert_alpha()

class Surface:
    def __init__(self,blit_window,blit_surface,surface_size=[1920,1080],background_size=[1920,1080],info_size=[1920,1080],gui_size=[1920,1080],popup_size=[1920,1080],transition_size=[1920,1080],window_size=[1920,1080]):
        self.blit_window = blit_window
        self.blit_surface = blit_surface
        
        self.surface_size = surface_size
        self.background_size = background_size
        self.info_size = info_size
        self.gui_size = gui_size
        self.popup_size = popup_size
        self.transition_size = transition_size
        self.window_size = window_size

        self.background_surface = pygame.Surface(self.background_size).convert_alpha()
        self.info_surface = pygame.Surface(self.info_size).convert_alpha()
        self.gui_surface = pygame.Surface(self.gui_size).convert_alpha()
        self.popup_surface = pygame.Surface(self.popup_size).convert_alpha()
        self.transition_surface = pygame.Surface(self.transition_size).convert_alpha()

    def blit(self):
        self.blit_surface.blit(self.background_surfaceFin, (0, 0))
        self.blit_surface.blit(self.info_surface, (0, 0))
        self.blit_surface.blit(self.gui_surface, (0, 0))
        self.blit_surface.blit(self.popup_surface, (0, 0))
        self.blit_surface.blit(self.transition_surface, (0, 0))

        self.blit_window.blit(self.blit_surface, (0, 0))

        pygame.display.update()

    def background(self):
        self.background_surface.fill((255,55,55,0))
        self.background_surface.fill((255,55,55,255))
        self.background_surface.blit(icon1,(0,0))

        self.background_surfaceFin = pygame.transform.scale(self.background_surface,self.window_size)
        
    def info(self):
        self.info_surface.fill((255,55,55,0))

        self.info_surfaceFin = pygame.transform.scale(self.info_surface,self.window_size)

    def gui(self):
        self.gui_surface.fill((255,55,55,0))

        self.gui_surfaceFin = pygame.transform.scale(self.gui_surface,self.window_size)

    def popup(self):
        self.popup_surface.fill((255,55,55,0))

        self.popup_surfaceFin = pygame.transform.scale(self.popup_surface,self.window_size)

    def transition(self):
        self.transition_surface.fill((255,55,55,0))

        self.transition_surfaceFin = pygame.transform.scale(self.transition_surface,self.window_size)