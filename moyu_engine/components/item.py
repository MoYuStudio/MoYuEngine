
import moyu_engine.config.global_config as G

import pygame
from pygame.locals import *

class Item:
    def __init__(self):

        self.name = 'item'
        self.type = 'item'

        self.default_image = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')
        self.preclick_image = None
        self.click_image = None

        self.blit_surface = None

        self.pos = [0,0]
        self.area = [64,64]
        
        self.collision_type = 'item'
        self.collision_with = []
        self.collision_preview = True
        self.collision_preview_width = 3
        self.collision_preview_width_color = (155,255,55,30)

    def blit(self,blit_surface):
        self.blit_surface = blit_surface

        self.ruct = pygame.Rect((self.pos[0],self.pos[1],self.area[0],self.area[1]),width=0)

        self.blit_surface.blit(self.default_image,self.ruct)

        if self.collision_preview == True:
            pygame.draw.rect(self.blit_surface,self.collision_preview_width_color,self.ruct,self.collision_preview_width)
        if self.collision_preview == False:
            pass

        if pygame.Rect.collidepoint(self.ruct,G.mouse_click_pos) == False and pygame.Rect.collidepoint(self.ruct,G.mouse_motion_pos) ==False:
            self.collision_preview_width_color = (155,255,55,30)
        if pygame.Rect.collidepoint(self.ruct,G.mouse_motion_pos) == True:
            self.collision_preview_width_color = (255,215,55,30)
            print('motion')
        if pygame.Rect.collidepoint(self.ruct,G.mouse_click_pos) == True:
            self.collision_preview_width_color = (255,55,55,30)
            print('click')

    def event(self):
        pass

    def collision(self):
        pass

if __name__ == '__main__':
    pass
