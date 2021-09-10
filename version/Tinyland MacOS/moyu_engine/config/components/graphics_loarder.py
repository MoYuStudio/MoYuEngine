
import os
import pygame

import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G

def tileland_graphics_loader(path):
    tileland_graphics_file_name = os.listdir(path)
    for i in range(0, len(tileland_graphics_file_name)):
        tileland_graphics_name = str(path) + tileland_graphics_file_name[i]
        print(tileland_graphics_name)
        C.tileland_graphics_path[i] = pygame.image.load(tileland_graphics_name).convert_alpha()
        C.tileland_graphics.append(C.tileland_graphics_path[i])