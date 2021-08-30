
import pygame

import constants as C

tl1 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL1.png').convert_alpha()

tl6 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL6.png').convert_alpha()

tl11 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL11.png').convert_alpha()

tl16 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL16.png').convert_alpha()

tl21 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL21.png').convert_alpha()

t105 = pygame.image.load('moyu_engine/assets/graphics/tile/T105.png').convert_alpha()

pretile_choose = pygame.image.load('moyu_engine/assets/graphics/pretile/Pretilechoose.png').convert_alpha()

pretile_green = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileGreen.png').convert_alpha()

pretile_red = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileRed.png').convert_alpha()

# === GUI ===

home_button = pygame.image.load('moyu_engine/assets/graphics/gui/home_button.png').convert_alpha()
home_buttonFin = pygame.transform.scale(home_button, (32,32))

button001 = pygame.image.load('moyu_engine/assets/graphics/gui/button001.png').convert_alpha()
button001Fin = pygame.transform.scale(button001, (64,64))
button001mini = pygame.image.load('moyu_engine/assets/graphics/gui/button001.png').convert_alpha()
button001miniFin = pygame.transform.scale(button001mini, (48,48))

money_icon = pygame.image.load('moyu_engine/assets/graphics/gui/money_icon.png').convert_alpha()
#money_icon.set_colorkey(0,0,0)
money_iconFin = pygame.transform.scale(money_icon, (32,32))

background = pygame.image.load('moyu_engine/assets/graphics/background/background.png').convert_alpha()
backgroundFin = pygame.transform.scale(background, (1280*3,720*3))