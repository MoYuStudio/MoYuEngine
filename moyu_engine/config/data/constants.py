
import pygame
from pygame.locals import *

window =\
{
    # window
    'size' : [1280,720],
    'fps'  : 60,
    'title': 'Tinyland 弹丸之地',

    # move
    'move':[0,0],
    'move_speed':10,
    'move_switch':
    {
        'up'   : False,
        'down' : False,
        'left' : False,
        'right': False,
    },
    'zoom_switch':
    {
        'in' : False,
        'out': False,
    },

    # window ppt
    'ppt_switch' : 0
    

}

tilemap =\
{
    # tilemap
    'tilemap': [],
    'boarder': 64,
    'seed'   : 0,
    'octaves': 2,
    'freq'   : 12,

    # tile
    'tile_size'       : 64,
    'pretile_type'    : 0,
    'tile_type'       : 0,
    'build'           : False,
    'reward'          : False,
    'tile_choose'     : False,
    'tile_choose_info': [0,0,0],
    'tile_choose_info': [0,0,0,0,0,0],
    
    # tile time
    'time_speed': 100,
}

assets =\
{
    'tile':
    {
        'tileland'    : [],
        'tilebuilding': [],
    },
    'gui':
    {
        'button': [],
        'input' : [],
    },
}

screen = pygame.display.set_mode(window['size'],pygame.RESIZABLE)

