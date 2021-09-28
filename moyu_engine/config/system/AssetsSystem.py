
import os
import sys
import pygame
from pygame.locals import *

import data.constants as C

class AssetsSystem:

    pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)

    @ staticmethod
    def input_all():
        AssetsSystem.font_en()
        AssetsSystem.font_zh()
        AssetsSystem.tile_tileland()
        AssetsSystem.gui_button()
        AssetsSystem.input_button()
        AssetsSystem.background()

    @ staticmethod
    def font_en():
        
        path = 'moyu_engine/assets/font/en'
        filenum = len(os.listdir(path))
        for num in range(0,filenum,1):
            C.assets['font']['en'].append(pygame.font.Font(os.path.join(path, f'en{num}.ttf'),25))

    @ staticmethod
    def font_zh():
        
        path = 'moyu_engine/assets/font/zh'
        filenum = len(os.listdir(path))-1
        for num in range(0,filenum,1):
            C.assets['font']['zh'].append(pygame.font.Font(os.path.join(path, f'zh{num}.ttf'),25))

    @ staticmethod
    def tile_tileland():
        
        tile_tileland_path = 'moyu_engine/assets/graphics/tile/tileland'
        tile_tileland_filenum = len(os.listdir(tile_tileland_path))-1
        for num in range(0,tile_tileland_filenum,1):
            C.assets['tile']['tileland'].append(pygame.image.load(os.path.join(tile_tileland_path, f'tl{num}.png')).convert_alpha())
    
    @ staticmethod
    def gui_button():
        
        gui_button_path = 'moyu_engine/assets/graphics/gui/button'
        gui_button_filenum = len(os.listdir(gui_button_path))
        for num in range(0,gui_button_filenum,1):
            C.assets['gui']['button'].append(pygame.image.load(os.path.join(gui_button_path, f'button{num}.png')).convert_alpha())

    @ staticmethod
    def input_button():
        
        input_button_path = 'moyu_engine/assets/graphics/gui/input'
        input_button_filenum = len(os.listdir(input_button_path))
        for num in range(0,input_button_filenum,1):
            C.assets['gui']['input'].append(pygame.image.load(os.path.join(input_button_path, f'input{num}.png')).convert_alpha())

    @ staticmethod
    def background():
        
        background_path = 'moyu_engine/assets/graphics/background'
        background_filenum = len(os.listdir(background_path))
        for num in range(0,background_filenum,1):
            C.assets['background'].append(pygame.image.load(os.path.join(background_path, f'background{num}.png')).convert_alpha())


if __name__ == "__main__":

    assets = AssetsSystem()
    assets.tileland()
    print(C.assets)
