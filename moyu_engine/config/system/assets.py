
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
