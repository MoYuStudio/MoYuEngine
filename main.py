
import moyu_engine

import pygame

gui = moyu_engine.system.gui_system.GuiSystem()
gui.config['window']['title'] = 'Tinyland'
gui.config['window']['size'] = [1280,720]

surface = pygame.Surface([1280,720]).convert_alpha()
gui.config['surface']['blit_surface'] = surface

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

gui.config['ui']['blit_window'] = gui.surface.gui_surface
gui.config['ui']['ui_event_preview'] = True
gui.config['ui']['button_image'] = pygame.image.load('tinyland\\assets\\graphics\\gui\\input\\input18.png')
gui.config['ui']['display_pos'] = [0,0]

gui.ui.button()

def surface_blit():
    
    gui.surface.background_surface.fill((255,255,255,255))
    gui.surface.background_surface.blit(icon1,(gui.config['event']['move']))
    gui.ui.button_blit()

def event_blit():
    
    gui.config['ui']['click_pos'] = gui.config['event']['mouse_click_pos']
    gui.config['ui']['motion_pos'] = gui.config['event']['mouse_motion_pos']

gui.set(surface_blit,event_blit)





# data = moyu_engine.components.data.Data()
# data.config['xlsx_path'] = r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\tinyland\data\tile.xlsx'
# data.xlsx()
# print(data.data)
