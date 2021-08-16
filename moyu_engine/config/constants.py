
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

tilemap_surface_level = 20
# 320 180 n = 20        16*n  9*n
tilemap_surface_size = [16*tilemap_surface_level,9*tilemap_surface_level]
tilemap_surface = pygame.Surface(tilemap_surface_size)

gui_surface_level = 20
# 320 180 n = 20        16*n  9*n
gui_surface_size = [16*gui_surface_level,9*gui_surface_level]
gui_surface = pygame.Surface(gui_surface_size)

