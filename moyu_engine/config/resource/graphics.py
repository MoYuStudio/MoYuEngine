
import pygame

import data.constants as C

pygame.init()

C.screen = pygame.display.set_mode((C.WINDOW_SIZE))

# == = Tileland == = 

tl1 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL1.png').convert_alpha()

tl6 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL6.png').convert_alpha()

tl11 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL11.png').convert_alpha()

tl16 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL16.png').convert_alpha()

tl21 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL21.png').convert_alpha()

# == = Tile == = 

t1      = pygame.image.load('moyu_engine/assets/graphics/tile/T1.png').convert_alpha()
t1_icon = pygame.transform.scale(t1, (48,24))

t2      = pygame.image.load('moyu_engine/assets/graphics/tile/T2.png').convert_alpha()
t2_icon = pygame.transform.scale(t2, (48,24))

t3      = pygame.image.load('moyu_engine/assets/graphics/tile/T3.png').convert_alpha()
t3_icon = pygame.transform.scale(t3, (48,24))

t4      = pygame.image.load('moyu_engine/assets/graphics/tile/T4.png').convert_alpha()
t4_icon = pygame.transform.scale(t4, (48,24))

t5      = pygame.image.load('moyu_engine/assets/graphics/tile/T5.png').convert_alpha()
t5_icon = pygame.transform.scale(t5, (48,24))

t105      = pygame.image.load('moyu_engine/assets/graphics/tile/T105.png').convert_alpha()
t105_icon = pygame.transform.scale(t105, (48,48))

t155      = pygame.image.load('moyu_engine/assets/graphics/tile/T155.png').convert_alpha()
t155_icon = pygame.transform.scale(t155, (48,48))

t205      = pygame.image.load('moyu_engine/assets/graphics/tile/T205.png').convert_alpha()
t205_icon = pygame.transform.scale(t205, (48,48))

# == = Pretile == = 

pretile_choose = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileChoose.png').convert_alpha()

pretile_green = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileGreen.png').convert_alpha()

pretile_red = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileRed.png').convert_alpha()

pretile_reward = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileReward.png').convert_alpha()

# == = GUI == = 

home_button    = pygame.image.load('moyu_engine/assets/graphics/gui/home_button.png').convert_alpha()
home_buttonFin = pygame.transform.scale(home_button, (64,64))

button    = pygame.image.load('moyu_engine/assets/graphics/gui/button.png').convert_alpha()
buttonFin = pygame.transform.scale(button, (64*3,16*3))

button001_unclick     = pygame.image.load('moyu_engine/assets/graphics/gui/button001_unclick.png').convert_alpha()
button001_unclickFin  = pygame.transform.scale(button001_unclick, (64*3,16*3))
button001_preclick    = pygame.image.load('moyu_engine/assets/graphics/gui/button001_preclick.png').convert_alpha()
button001_preclickFin = pygame.transform.scale(button001_preclick, (64*3,16*3))
button001_clicked     = pygame.image.load('moyu_engine/assets/graphics/gui/button001_clicked.png').convert_alpha()
button001_clickedFin  = pygame.transform.scale(button001_clicked, (64*3,16*3))

button001        = pygame.image.load('moyu_engine/assets/graphics/gui/button001.png').convert_alpha()
button001Fin     = pygame.transform.scale(button001, (64,64))
button001mini    = pygame.image.load('moyu_engine/assets/graphics/gui/button001.png').convert_alpha()
button001miniFin = pygame.transform.scale(button001mini, (48,48))

money_icon = pygame.image.load('moyu_engine/assets/graphics/gui/money_icon.png').convert_alpha()
#money_icon.set_colorkey(0,0,0)
money_iconFin = pygame.transform.scale(money_icon, (32,32))

background    = pygame.image.load('moyu_engine/assets/graphics/background/background.png').convert_alpha()
backgroundFin = pygame.transform.scale(background, (1280*3,720*3))

menu_background    = pygame.image.load('moyu_engine/assets/graphics/background/menu_background.png').convert_alpha()
menu_backgroundFin = pygame.transform.scale(menu_background, (1920,1080))