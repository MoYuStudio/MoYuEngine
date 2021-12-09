
import sys 
sys.path.append('moyu_engine') 

import components as c

import pygame

class GuiSystem():
    def __init__(self):
        
        self.window = c.window.Window()
        self.surface = c.surface.Surface()
        self.page = c.page.Page()
        self.event = c.event.Event()

        self.config = {
                        'window':self.window.config,
                        'surface':self.surface.config,
                        'page':self.page.config,
                        'event':self.event.config,
                        }

    def set(self):

        self.config['page']['page_switch']['main_mean_page'] = False
        self.config['page']['page']['main_mean_page'] = pygame.Surface(self.config['window']['size']).convert_alpha()
        self.config['page']['page_switch']['main_game_page'] = False
        self.config['page']['page']['main_game_page'] = pygame.Surface(self.config['window']['size']).convert_alpha()
        self.config['page']['page_switch']['main_mean_page'] = False
        self.config['page']['page']['main_mean_page'] = pygame.Surface(self.config['window']['size']).convert_alpha()

    def blit(self,suface_blit,event_blit):
        
        while True:
            
            self.window.set()
            self.surface.config['blit_window'] = self.window.screen

            self.surface.blit()
            self.event.blit()

            suface_blit()
            self.event.set()
            event_blit()

if __name__=="__main__":
    gui = GuiSystem()
    gui.set()
    gui.blit()