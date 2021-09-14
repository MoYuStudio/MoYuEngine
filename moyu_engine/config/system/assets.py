
import pygame

import system.setting as S

pygame.init()

S.SCREEN = pygame.display.set_mode(S.WINDOW_SIZE)

# Background ============================================================================ = 

menu_background    = pygame.image.load('moyu_engine/assets/graphics/background/menu_background.png').convert_alpha()
menu_backgroundFin = pygame.transform.scale(menu_background, (1280,720))

# GUI ================================================================ = 

font1 = pygame.font.Font('moyu_engine/assets/font/方正像素16.TTF', 25)

button001_unclick     = pygame.image.load('moyu_engine/assets/graphics/gui/button001_unclick.png').convert_alpha()
button001_unclickFin  = pygame.transform.scale(button001_unclick, (64*3,16*3))
button001_preclick    = pygame.image.load('moyu_engine/assets/graphics/gui/button001_preclick.png').convert_alpha()
button001_preclickFin = pygame.transform.scale(button001_preclick, (64*3,16*3))
button001_clicked     = pygame.image.load('moyu_engine/assets/graphics/gui/button001_clicked.png').convert_alpha()
button001_clickedFin  = pygame.transform.scale(button001_clicked, (64*3,16*3))

button_sound = pygame.mixer.Sound('moyu_engine/assets/sound/click5.ogg')
