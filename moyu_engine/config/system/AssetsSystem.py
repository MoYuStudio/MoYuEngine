
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

class AssetsSystem:

    pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)

    @ staticmethod
    def input_all():
        AssetsSystem.tileland()
        AssetsSystem.gui_button()
        AssetsSystem.input_button()

    @ staticmethod
    def tileland():
        
        tileland_path = 'moyu_engine/assets/graphics/tileland'
        tileland_filenum = len(os.listdir(tileland_path))-1
        for num in range(tileland_filenum):
            C.assets['tileland'].append(pygame.image.load(os.path.join(tileland_path, f'tl{num}.png')).convert_alpha())

    @ staticmethod
    def gui_button():
        
        gui_button_path = 'moyu_engine/assets/graphics/gui/button'
        gui_button_filenum = len(os.listdir(gui_button_path))-1
        for num in range(gui_button_filenum):
            C.assets['gui']['button'].append(pygame.image.load(os.path.join(gui_button_path, f'button{num}.png')).convert_alpha())

    @ staticmethod
    def input_button():
        
        input_button_path = 'moyu_engine/assets/graphics/gui/input'
        input_button_filenum = len(os.listdir(input_button_path))-1
        for num in range(input_button_filenum):
            C.assets['gui']['input'].append(pygame.image.load(os.path.join(input_button_path, f'input{num}.png')).convert_alpha())

if __name__ == "__main__":

    assets = AssetsSystem()
    assets.tileland()
    print(C.assets)
