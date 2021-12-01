
import moyu_engine

import pygame

gui = moyu_engine.system.gui_system.GuiSystem()
gui.gui_system_data['window_data']['title'] = 'Tinyland'
surface = pygame.Surface([1280,720]).convert_alpha()
gui.gui_system_data['surface_data']['blit_surface'] = surface

icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png')#.convert_alpha()

gui.surface.background_surface.fill((255,55,55,255))
gui.surface.background_surface.blit(icon1,(100,100))

gui.set()