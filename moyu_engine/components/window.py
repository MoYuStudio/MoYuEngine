
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png')#.convert_alpha()

class Window:
    def __init__(self,window_set = {
                                        'icon':icon1,
                                        'title':'MoYu Engine',
                                        'size':[320,180],
                                        'resizable':True,
                                    }):
        self.window_set = window_set

    def set(self):
        if self.window_set['resizable'] == True:
            self.screen = pygame.display.set_mode(self.window_set['size'],pygame.RESIZABLE)
        if self.window_set['resizable'] == False:
            self.screen = pygame.display.set_mode(self.window_set['size'])
        screen_title = pygame.display.set_caption(self.window_set['title'])
        icon = pygame.display.set_icon(self.window_set['icon'])
        clock = pygame.time.Clock()

        return self.screen

if __name__=="__main__":
    window = Window()
    window.set()