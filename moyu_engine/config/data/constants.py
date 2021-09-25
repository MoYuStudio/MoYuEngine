
import pygame
from pygame.locals import *

window = \
{
'size' : [1280,720],
'fps'  : 60,
'title': 'Tinyland 弹丸之地',
}

screen = pygame.display.set_mode(window['size'],pygame.RESIZABLE)

assets_tileland = []