
import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

class Window:
    def __init__(self,config = {
                                        'icon':icon1,
                                        'title':'MoYu Engine',
                                        'size':[320,180],
                                        'resizable':True,
                                    }):
        self.config = config

    def set(self):
        if self.config['resizable'] == True:
            self.screen = pygame.display.set_mode(self.config['size'],pygame.RESIZABLE)
        if self.config['resizable'] == False:
            self.screen = pygame.display.set_mode(self.config['size'])
        screen_title = pygame.display.set_caption(self.config['title'])
        icon = pygame.display.set_icon(self.config['icon'])
        clock = pygame.time.Clock()

        return self.screen

if __name__=="__main__":
    window = Window()
    window.set()