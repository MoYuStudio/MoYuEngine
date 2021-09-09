
import pygame

import moyu_engine.config.constants as C

def fade(): 
    fade = pygame.Surface((C.window_size))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        C.screen.blit(fade, (0,0))
        pygame.time.delay(5)
