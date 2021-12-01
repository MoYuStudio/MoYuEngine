
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png')#.convert_alpha()

class Window:
    def __init__(self,window_data = {
                                        'icon':icon1,
                                        'title':'MoYu Engine',
                                        'size':[320,180],
                                        'resizable':True,
                                    }):
        self.window_data = window_data

    def set(self):
        if self.window_data['resizable'] == True:
            self.screen = pygame.display.set_mode(self.window_data['size'],pygame.RESIZABLE)
        if self.window_data['resizable'] == False:
            self.screen = pygame.display.set_mode(self.window_data['size'])
        screen_title = pygame.display.set_caption(self.window_data['title'])
        icon = pygame.display.set_icon(self.window_data['icon'])
        clock = pygame.time.Clock()

        return self.screen

if __name__=="__main__":
    window = Window()
    window.set()