
import moyu_engine

import pygame

gui = moyu_engine.system.gui_system.GuiSystem()
gui.config['window']['title'] = 'Tinyland'
gui.config['window']['size'] = [1280,720]

surface = pygame.Surface([1280,720]).convert_alpha()
gui.config['surface']['blit_surface'] = surface

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

def blit():
    gui.surface.background_surface.fill((255,55,55,255))
    gui.surface.background_surface.blit(icon1,(gui.config['event']['move']))

gui.set(blit)





# data = moyu_engine.components.data.Data()
# data.config['xlsx_path'] = r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\tinyland\data\tile.xlsx'
# data.xlsx()
# print(data.data)
