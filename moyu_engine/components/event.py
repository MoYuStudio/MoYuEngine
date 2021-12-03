
import sys
import pygame
from pygame.locals import *

class Event:
    def __init__(self,config={
                                    'move':[0,0],
                                    'zoom':0,
                                    'move_speed':10,
                                }):
        self.config = config

    def set(self):
        for self.event in pygame.event.get():
            if self.event.type == QUIT:
                pygame.quit()
                sys.exit()

            if self.event.type == pygame.KEYDOWN:
                self.move_keydown()
            if self.event.type == pygame.KEYUP:
                self.move_keyup()

    def move_keydown(self):
        if self.event.key == K_UP or self.event.key == K_w:
            self.config['move'][1] += self.config['move_speed']
            
        if self.event.key == K_DOWN or self.event.key == K_s:
            self.config['move'][1] -= self.config['move_speed']

        if self.event.key == K_LEFT or self.event.key == K_a:
            self.config['move'][0] += self.config['move_speed']

        if self.event.key == K_RIGHT or self.event.key == K_d:
            self.config['move'][0] -= self.config['move_speed']

        return self.config

    def move_keyup(self):
        if self.event.key == K_UP or self.event.key == K_w:
            pass

        if self.event.key == K_DOWN or self.event.key == K_s:
            pass

        if self.event.key == K_LEFT or self.event.key == K_a:
            pass

        if self.event.key == K_RIGHT or self.event.key == K_d:
            pass

    def zoom_keydown(self):
        if self.event.key == K_q:
            if self.config['surface_level'] <= 0.25:
                self.config['surface_level'] = 0.25
            else:
                self.config['surface_level'] -= 0.025
                self.config['move'][1] -= 4.25
                self.config['move'][0] -= 7.9

        if self.event.key == K_e:
            if self.config['surface_level'] >= 1:
                self.config['surface_level'] = 1
            else:
                self.config['surface_level'] += 0.025
                self.config['move'][1] += 4.25
                self.config['move'][0] += 7.9

    def zoom_keyup(self):
        if self.event.key == K_q:
            pass

        if self.event.key == K_e:
            pass
        
if __name__ == "__main__":
    pass
