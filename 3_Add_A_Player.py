
import moyu_engine

import pygame
player = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')

window = moyu_engine.window.Window()
surface = moyu_engine.surface.Surface()
event = moyu_engine.event.Event()

window.title = 'MY FIRST GAME 我的第一个游戏'

def BackgroundPage():

    print(event.move_pos)

    surface.surface.fill((154,255,154))
    surface.surface.blit(player,(event.move_pos))
    surface.blit(window.screen)

    event.move_switch()

def PlayerEvent():

    event.move_key(window.key_event)

window.blit = BackgroundPage
window.event = PlayerEvent
window.set()
