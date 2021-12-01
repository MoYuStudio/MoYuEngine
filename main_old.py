
import moyu_engine
import moyu_engine.components as c

import pygame
from pygame.locals import *

a = {'test':232}
b = {}
surface1 = pygame.Surface([1280,720])#.convert_alpha()
icon1 = pygame.image.load('moyu_engine/assets/graphics/tileland1.png')#.convert_alpha()

win = c.window.Window()
win.window_set['title']='ahe'
win.set()

pygame.display.flip()

sur = c.surface.Surface()
sur.surface_set['blit_window'] = win.screen
sur.surface_set['blit_surface'] = surface1


ev = c.event.Event()
save = c.save.Save(slot_name='save',write_data=a)

save.write()
save.read()

b = save.read_data
# b = b.decode()

print('=',b['test'])


sur.background_surface.fill((255,55,55,255))
sur.background_surface.blit(icon1,(0,0))
sur.background()

while True:
    sur.blit()
    ev.quit()