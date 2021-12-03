
import moyu_engine

import pygame

gui = moyu_engine.system.gui_system.GuiSystem()
gui.gui_system_data['window_data']['title'] = 'Tinyland'
gui.gui_system_data['window_data']['size'] = [1920,1080]
surface = pygame.Surface([1920,1080]).convert_alpha()
gui.gui_system_data['surface_data']['blit_surface'] = surface

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

gui.surface.background_surface.fill((255,55,55,255))
gui.surface.background_surface.blit(icon1,(100,100))

data = moyu_engine.components.data.Data()
data.data_data['xlsx_path'] = r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\tinyland\data\tile.xlsx'
data.xlsx()
print(data.data[0])

gui.set()

