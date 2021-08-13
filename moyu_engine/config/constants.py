
import pygame

boarder = 16
#tile_level = 1
tile_size = 64 #*tile_level
move_x,move_y = 0,0
move_speed = 5

tile_choose_info = [0,0,0,0,0,0]

mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2)),(boarder/2*(tile_size/4)+boarder/2*(tile_size/4))

mouse_pos_x,mouse_pos_y = 0,0

move_up = False
move_down = False
move_left = False
move_right = False

buildable_preview = False

window_size = [1280,720]
screen = pygame.display.set_mode(window_size)
screen_title = pygame.display.set_caption('TinyLand 弹丸之地')

clock = pygame.time.Clock()

tilemap = []

tile_choose_info = [0,0,0,0,0,0,0,0,0]

# Surface

tilemap_surface = pygame.Surface((320,180))

