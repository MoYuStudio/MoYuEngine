
import moyu_engine

# ToDo: 目前新版引擎对pygame资源导入部分还未封装完毕
import pygame
player = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')
# ===========================================================

G = moyu_engine.global_config
G.window_size = [320*2,180*2]

window = moyu_engine.Window()
surface = moyu_engine.Surface()
event = moyu_engine.Event()
item = moyu_engine.Item()
play = moyu_engine.Item()

window.title = 'MY FIRST GAME 我的第一个游戏'

item.pos = [100,100]

event.move_switch = True

def BackgroundPage():

    surface.surface.fill((154,255,154))
    #surface.surface.blit(player,(event.move_pos))
    play.pos = (event.move_pos)
    play.blit(surface.surface)
    item.blit(surface.surface)

    surface.blit(window.screen)
    event.blit()

def PlayerEvent():
    event.input(window.input_event)

window.blit = BackgroundPage
window.event = PlayerEvent
window.set()