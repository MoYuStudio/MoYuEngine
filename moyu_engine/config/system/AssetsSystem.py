
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

class AssetsSystem:

    pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)

    @ staticmethod
    def tileland():
        
        tileland_path = 'moyu_engine/assets/graphics/tileland'
        tileland_filenum = len(os.listdir(tileland_path))-1
        for num in range(tileland_filenum):
            C.assets['tileland'].append(pygame.image.load(os.path.join(tileland_path, f'tl{num}.png')).convert_alpha())

if __name__ == "__main__":

    assets = AssetsSystem()
    assets.tileland()
    print(C.assets)
