
import pygame

class Event:

    def __init__(self):
        
        self.move_pos = [0,0]
        self.zoom_level = 0
        self.move_speed = 10
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.zoom_in = False
        self.zoom_out = False

    def move(self):
        if self.move_up == True:
            self.move_pos[1] -= self.move_speed
        if self.move_down == True:
            self.move_pos[1] += self.move_speed
        if self.move_left == True:
            self.move_pos[0] -= self.move_speed
        if self.move_right == True:
            self.move_pos[0] += self.move_speed

    def move_keydown(self):

        if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
            self.move_up = True
        if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
            self.move_down = True
        if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
            self.move_left = True
        if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
            self.move_right = True

    def move_keyup(self):

        if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
            self.move_up   = False
        if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
            self.move_down = False
        if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
            self.move_left = False
        if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
            self.move_right = False