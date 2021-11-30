
import moyu_engine
import moyu_engine.components as c

import pygame
from pygame.locals import *

a = {'test':232}
b = {}
surface1 = pygame.Surface([1280,720])#.convert_alpha()

win = c.window.Window()
win.set()
n = win.screen
print(n)
sur = c.surface.Surface(n,surface1)
ev = c.event.Event()
save = c.save.Save(slot_name='save',write_data=a)

save.write()
save.read()

b = save.read_data
# b = b.decode()

print('=',b['test'])



sur.background()

while True:
    sur.blit()
    ev.quit()