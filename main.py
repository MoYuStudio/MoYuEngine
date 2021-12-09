
import moyu_engine

import pygame

gui = moyu_engine.system.gui_system.GuiSystem()
gui.config['window']['title'] = 'Tinyland'
gui.config['window']['size'] = [320*3,180*3]

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

ui1 = moyu_engine.components.ui.Ui()
ui1.config['blit_window'] = gui.surface.gui_surface
ui1.config['ui_event_preview'] = True
ui1.config['button_image'] = pygame.image.load('tinyland/assets/graphics/gui/input/input18.png')
ui1.config['display_pos'] = [100,100]
ui1.config['button_area'] = [100,30]

ui2 = moyu_engine.components.ui.Ui()
ui2.config['blit_window'] = gui.surface.gui_surface
ui2.config['ui_event_preview'] = True
ui2.config['button_image'] = pygame.image.load('tinyland/assets/graphics/gui/input/input19.png')
ui2.config['display_pos'] = [500,500]
ui2.config['button_area'] = [300,100]

def surface_blit():
    
    gui.surface.background_surface.fill((255,255,255,255))
    gui.surface.background_surface.blit(icon1,(gui.config['event']['move']))
    # gui.ui.button_blit()
    ui1.button_blit()
    ui2.button_blit()

def event_blit():

    ui1.config['click_pos'] = gui.config['event']['mouse_click_pos']
    ui1.config['motion_pos'] = gui.config['event']['mouse_motion_pos']

    ui2.config['click_pos'] = gui.config['event']['mouse_click_pos']
    ui2.config['motion_pos'] = gui.config['event']['mouse_motion_pos']

ui1.button_set()
ui2.button_set()
gui.set()
gui.config['surface']['blit_surface'] = gui.config['page']['page']['main_mean_page']

gui.blit(surface_blit,event_blit)





# data = moyu_engine.components.data.Data()
# data.config['xlsx_path'] = r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\tinyland\data\tile.xlsx'
# data.xlsx()
# print(data.data)
