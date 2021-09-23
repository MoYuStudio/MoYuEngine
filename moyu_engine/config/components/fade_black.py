
import pygame

import moyu_engine.config.constants as C

def fade_black_blit():

    C.fade_black_surface.fill((0,0,0))
    C.SCREEN.blit(C.fade_black_surface, (0,0))

def fade_black_surface():
    if C.fade_black == True:
        if C.fade_black_alpha <= 0 :
            C.fade_black_alpha += 10
            C.fade_black_surface.set_alpha(C.fade_black_alpha)

        if C.fade_black_alpha >= 255:
            C.fade_black = False
            C.fade_black_alpha = 0
            C.window_switch = True

'''
def fade(): 
    fade = pygame.Surface((C.window_size))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        C.screen.blit(fade, (0,0))
        pygame.time.delay(5)

def fade_black1():

    if C.fade_black == True:
        if C.alpha >= -100 :
            C.alpha -= 10
            C.MENUmain_surface.set_alpha(C.alpha)
        if 0 >= C.alpha >= -100:
            C.fade_black = False
            C.alpha = 255
            C.window_switch = True

            if C.window_switch == True and C.buttonStartGame == True:
                C.MENUmain = False
                C.GAMEmain = True

                C.window_switch = False
                C.buttonStartGame = False
'''