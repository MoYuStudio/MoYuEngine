
import pygame

boarder = 16
#tile_level = 1
tile_size = 64 #*tile_level
move_x,move_y = 450,5
move_speed = 5

tile_choose_info = [0,0,0,0,0,0]

#mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2)),(boarder/2*(tile_size/4)+boarder/2*(tile_size/4))

mouse_pos_x,mouse_pos_y = 0,0
mouse_down_pos_x,mouse_down_pos_y = 0,0 

move_up = False
move_down = False
move_left = False
move_right = False

zoom_in = False
zoom_out = False

window_size = [1280,720]
screen = pygame.display.set_mode(window_size)
screen_title = pygame.display.set_caption('TinyLand 弹丸之地')

clock = pygame.time.Clock()

tilemap = []

tile_choose = False
tile_choose_info = [0,0,0]

# ================================================= Surface =================================================

game_main_surface_level = 60
# 320 180 n = 20        16*n  9*n    1280 720 n = 80
game_main_surface_size = [16*game_main_surface_level,9*game_main_surface_level]
game_main_surface = pygame.Surface(game_main_surface_size)

# ================================================= Scrollbar =================================================

scrollbar_line_color = [255, 255, 255]
scrollbar_line_pos = [50, 50]
scrollbar_line_size = [3, 250]

scrollbar_button_color = [161, 136, 127]
scrollbar_button_pos = [44, 50]
scrollbar_button_size = [15, 20]

scrollbar_moveable = False
scrollbar_move = 0