
import moyu_engine.config.global_config as G

import pygame
from pygame.locals import *

class Event:

    def __init__(self):
        
        self.move_pos = [0,0]
        self.zoom_level = 0
        self.move_speed = 0.1

        self.move_switch = False
        self.zoom_switch = False

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.zoom_in = False
        self.zoom_out = False

    def input(self,input_event):
        self.input_event = input_event

        if self.input_event.type == pygame.MOUSEMOTION:
            G.mouse_motion_pos = self.input_event.pos

        if self.input_event.type == pygame.MOUSEBUTTONDOWN:
            G.mouse_click_pos = self.input_event.pos

        if self.input_event.type == pygame.MOUSEBUTTONUP:
            G.mouse_click_pos = [-1,-1]

        if self.input_event.type == pygame.KEYDOWN:

            self.keydown()

            if self.input_event.key == pygame.K_UP or self.input_event.key == pygame.K_w:
                if self.move_switch == True:
                    self.move_up = True
            if self.input_event.key == pygame.K_DOWN or self.input_event.key == pygame.K_s:
                if self.move_switch == True:
                    self.move_down = True
            if self.input_event.key == pygame.K_LEFT or self.input_event.key == pygame.K_a:
                if self.move_switch == True:
                    self.move_left = True
            if self.input_event.key == pygame.K_RIGHT or self.input_event.key == pygame.K_d:
                if self.move_switch == True:
                    self.move_right = True

            if self.input_event.key == pygame.K_q:
                if self.zoom_switch == True:
                    self.zoom_in = True
            if self.input_event.key == pygame.K_e:
                if self.zoom_switch == True:
                    self.zoom_out = True



        if self.input_event.type == pygame.KEYUP:

            self.keyup()

            if self.input_event.key == pygame.K_UP or self.input_event.key == pygame.K_w:
                if self.move_switch == True:
                    self.move_up   = False
            if self.input_event.key == pygame.K_DOWN or self.input_event.key == pygame.K_s:
                if self.move_switch == True:
                    self.move_down = False
            if self.input_event.key == pygame.K_LEFT or self.input_event.key == pygame.K_a:
                if self.move_switch == True:
                    self.move_left = False
            if self.input_event.key == pygame.K_RIGHT or self.input_event.key == pygame.K_d:
                if self.move_switch == True:
                    self.move_right = False

            if self.input_event.key == pygame.K_q:
                if self.zoom_switch == True:
                    self.zoom_in = False
            if self.input_event.key == pygame.K_e:
                if self.zoom_switch == True:
                    self.zoom_out = False

    def blit(self):

        if self.move_switch == True:
            if self.move_up == True:
                self.move_pos[1] -= self.move_speed
            if self.move_down == True:
                self.move_pos[1] += self.move_speed
            if self.move_left == True:
                self.move_pos[0] -= self.move_speed
            if self.move_right == True:
                self.move_pos[0] += self.move_speed

        if self.zoom_switch == True:
            if self.zoom_in == True:
                if self.zoom_level <= 0.25:
                    self.zoom_level = 0.25
                else:
                    self.zoom_level -= 0.025
                    self.move_pos[1] -= 4.25
                    self.move_pos[0] -= 7.9
            if self.zoom_out == True:
                if self.zoom_level >= 1:
                    self.zoom_level = 1
                else:
                    self.zoom_level += 0.025
                    self.move_pos[1] += 4.25
                    self.move_pos[0] += 7.9

    def keydown(self):
        pass
    def keyup(self):
        pass

if __name__ == '__main__':
    pass