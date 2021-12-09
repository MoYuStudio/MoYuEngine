
import sys
import pygame
from pygame.locals import *

class Event:
    def __init__(self):
        self.config = {
                            'mouse_motion_pos':[-1,-1],
                            'mouse_click_pos':[-1,-1],
                            'move':[0,0],
                            'zoom':0,
                            'move_speed':10,

                            'move_switch':{
                                            'up':False,
                                            'down':False,
                                            'left':False,
                                            'right':False,
                            },
                            'zoom_switch':{
                                            'in':False,
                                            'out':False,
                            },
                        }

    def set(self):
        for self.event in pygame.event.get():
            
            if self.event.type == QUIT:
                pygame.quit()
                sys.exit()

            if self.event.type == pygame.MOUSEMOTION:
                self.config['mouse_motion_pos'] = self.event.pos

            if self.event.type == pygame.MOUSEBUTTONDOWN:
                self.config['mouse_click_pos'] = self.event.pos

            if self.event.type == pygame.MOUSEBUTTONUP:
                self.config['mouse_click_pos'] = [-1,-1]

            if self.event.type == pygame.KEYDOWN:
                self.move_keydown()
                
            if self.event.type == pygame.KEYUP:
                self.move_keyup()

        return self.config

    def blit(self):
        self.move()
        self.zoom()

    def move(self):
        if self.config['move_switch']['up'] == True:
            self.config['move'][1] -= self.config['move_speed']
        if self.config['move_switch']['down'] == True:
            self.config['move'][1] += self.config['move_speed']
        if self.config['move_switch']['left'] == True:
            self.config['move'][0] -= self.config['move_speed']
        if self.config['move_switch']['right'] == True:
            self.config['move'][0] += self.config['move_speed']

    def move_keydown(self):
        if self.event.key == K_UP or self.event.key == K_w:
            self.config['move_switch']['up']   = True
            
        if self.event.key == K_DOWN or self.event.key == K_s:
            self.config['move_switch']['down'] = True

        if self.event.key == K_LEFT or self.event.key == K_a:
            self.config['move_switch']['left'] = True

        if self.event.key == K_RIGHT or self.event.key == K_d:
            self.config['move_switch']['right'] = True

        return self.config

    def move_keyup(self):
        if self.event.key == K_UP or self.event.key == K_w:
            self.config['move_switch']['up']   = False

        if self.event.key == K_DOWN or self.event.key == K_s:
            self.config['move_switch']['down'] = False

        if self.event.key == K_LEFT or self.event.key == K_a:
            self.config['move_switch']['left'] = False

        if self.event.key == K_RIGHT or self.event.key == K_d:
            self.config['move_switch']['right'] = False

    def zoom(self):
        if self.config['zoom_switch']['in'] == True:
            if self.config['surface_level'] <= 0.25:
                self.config['surface_level'] = 0.25
            else:
                self.config['surface_level'] -= 0.025
                self.config['move'][1] -= 4.25
                self.config['move'][0] -= 7.9
        if self.config['zoom_switch']['out'] == True:
            if self.config['surface_level'] >= 1:
                self.config['surface_level'] = 1
            else:
                self.config['surface_level'] += 0.025
                self.config['move'][1] += 4.25
                self.config['move'][0] += 7.9

    def zoom_keydown(self):
        if self.event.key == K_q:
            self.config['zoom_switch']['in']   = True

        if self.event.key == K_e:
            self.config['zoom_switch']['out']  = True

    def zoom_keyup(self):
        if self.event.key == K_q:
            self.config['zoom_switch']['in']   = False

        if self.event.key == K_e:
            self.config['zoom_switch']['out'] = False

if __name__ == "__main__":
    pass
