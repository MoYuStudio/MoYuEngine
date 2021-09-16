
import pickle
import pygame

WINDOW_SIZE = (1280,720)
WINDOW_FPS = 60

SCREEN = pygame.display.set_mode(WINDOW_SIZE)

MOUSE_POS = [0,0]

SEED = 0
TILEMAP = []
BOARDER = 16

MONEY = 1000

TIME_SPEED = 100

REWARD = False

class SAVE:
    def auto_save():
        pass
    def setting_save():
        pass
    def game_save():
        f=open('moyu_engine/data/game_save','wb')
        save_data = {'map':TILEMAP}
        pickle.dump(save_data, f)
        f.close()

class LOAD:
    def start_load():
        pass
    def setting_load():
        pass
    def game_load():
        f=open('moyu_engine/data/game_save', 'rb')
        data = pickle.load(f)
        TILEMAP = data['map']
        f.close()