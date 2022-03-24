
from re import T
import moyu_engine.config.global_config as G

import pygame
from pygame.locals import *

class Item:
    def __init__(self):

        self.name = 'item' + str(G.item_name_timer)
        self.type = 'item'

        self.default_image = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')
        self.preclick_image = None
        self.click_image = None

        self.blit_surface = None

        self.pos = [0,0]
        self.area = [64,64]
        
        self.collision_mod = True
        self.collision_type = 'item'
        self.collision_with = ['item']
        self.collision_preview = True
        self.collision_preview_width = 3
        self.collision_preview_width_color = (155,255,55,30)

        G.item_name_timer += 1

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
        if pygame.Rect.collidepoint(self.ruct,G.mouse_click_pos) == True:
            self.collision_preview_width_color = (255,55,55,30)

        G.item_collision[self.collision_type].append(self.ruct)

        if self.collision_mod == True:
            self.move(self.ruct)

    def event(self):
        pass

    def collision(self,rect):
        self.collisions = []
        for collision_with_ones in self.collision_with:
            for collision_item in G.item_collision[collision_with_ones]:
                if rect.colliderect(collision_item):
                    self.collisions.append(collision_item)
        return self.collisions

    def move(self,rect):
        rect.x += G.movement[0]

        self.collisions = self.collision(rect)

        for tile in self.collisions:
            if G.movement[0] > 0:
                rect.right = tile.left
            if G.movement[0] < 0:
                rect.left = tile.right

        rect.y += G.movement[1]

        self.collisions = self.collision(rect)

        for tile in self.collisions:
            if G.movement[1] > 0:
                rect.bottom = tile.top
            if G.movement[1] < 0:
                rect.top = tile.bottom
                
        return rect

                #     if self.rect.colliderect(collision_item):
                #         collisions.append(collision_item)
                #         print(collisions)
                #     return collisions
                    # collision_item = G.item_collision[collision_with_ones][item_name]

                    # print(collision_item)

                    # if pygame.Rect.collidepoint(self.ruct,(collision_item['pos'][0],collision_item['pos'][1])) == True or \
                    #     pygame.Rect.collidepoint(self.ruct,(collision_item['pos'][0]+collision_item['area'][0],collision_item['pos'][1])) == True or \
                    #     pygame.Rect.collidepoint(self.ruct,(collision_item['pos'][0],collision_item['pos'][1]+collision_item['area'][1])) == True or \
                    #     pygame.Rect.collidepoint(self.ruct,(collision_item['pos'][0]+collision_item['area'][0],collision_item['pos'][1]+collision_item['area'][1])) == True :

                    #     self.collision_preview_width_color = (185,55,255,30)


if __name__ == '__main__':
    pass
