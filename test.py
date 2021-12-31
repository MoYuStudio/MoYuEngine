
import moyu_engine
import pygame

icon1 = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')#.convert_alpha()

gui = moyu_engine.system.gui_system.GuiSystem()


def surface_blit():
    
    gui.surface.background_surface.fill((255,255,255,255))
    gui.surface.background_surface.blit(icon1,(gui.config['event']['move']))


def event_blit():
    pass


gui.set()
gui.config['surface']['blit_surface'] = gui.config['page']['page']['main_mean_page']

gui.blit(surface_blit,event_blit)
