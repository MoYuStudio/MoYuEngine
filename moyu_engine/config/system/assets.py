
import pygame

import system.setting as S

pygame.init()

S.SCREEN = pygame.display.set_mode(S.WINDOW_SIZE)

# Background =============================================================================

menu_background    = pygame.image.load('moyu_engine/assets/graphics/background/menu_background.png').convert_alpha()
menu_backgroundFin = pygame.transform.scale(menu_background, (1280,720))
