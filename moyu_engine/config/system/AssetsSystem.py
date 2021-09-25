
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

class AssetsSystem:

    pygame.display.set_mode(C.window_size,pygame.RESIZABLE)

    def tileland(self):
        for num in range(4):
            C.assets_tileland.append(pygame.image.load(os.path.join('moyu_engine/assets/graphics/tileland', f'tl{num}.png')).convert_alpha())

if __name__ == "__main__":

    assets = AssetsSystem()
    assets.tileland()
    print(C.assets_tileland)
