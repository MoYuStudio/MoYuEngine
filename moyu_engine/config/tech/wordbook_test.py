
import sys
import pygame
from pygame.locals import *

mainwindow = pygame.display.set_mode((600,600))
window_title = pygame.display.set_caption('test')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

tile_level = 1.1

constants_set = {
    'tile_size' : 64 * tile_level,
}


constants = {
    'boarder' : 16,
    'move_x' : 19*30,
    'move_y' : 3*30,
    'move_speed' : 5,
}

print(constants_set['tile_size'])

tl1 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL1.png').convert_alpha()
tl1Fin = pygame.transform.scale(tl1, (64 * tile_level,64 * tile_level))

while True:

    mainwindow.fill((0,0,0))

    mainwindow.blit(tl1Fin,(100,100))
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

