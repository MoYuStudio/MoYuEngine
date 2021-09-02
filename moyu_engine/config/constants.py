
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
screen_title = pygame.display.set_caption('Tinyland 弹丸之地')

clock = pygame.time.Clock()

tilemap = []

tile_choose = False
tile_choose_info = [0,0,0]

# ================================================= Surface =================================================

game_main_surface_level = 60
# 320 180 n = 20        16*n  9*n    1280 720 n = 80
game_main_surface_size = [16*game_main_surface_level,9*game_main_surface_level]
game_main_surface = pygame.Surface(game_main_surface_size)

surface_level = (1280/(16*game_main_surface_level))


game_main_gui_surface_level = 80
# 320 180 n = 20        16*n  9*n    1280 720 n = 80
game_main_gui_surface_size = [16*game_main_gui_surface_level,9*game_main_gui_surface_level]
game_main_gui_surface = pygame.Surface(game_main_gui_surface_size)

#surface_level = (1280/(16*game_main_gui_surface_level))

menu_main_surface_level = 80
# 320 180 n = 20        16*n  9*n    1280 720 n = 80
menu_main_surface_size = [16*menu_main_surface_level,9*menu_main_surface_level]
menu_main_surface = pygame.Surface(menu_main_surface_size)


# ================================================= Scrollbar =================================================

scrollbar_line_color = [255, 255, 255]
scrollbar_line_pos = [85, 10]
scrollbar_line_size = [3, 360]

scrollbar_button_color = [161, 136, 127]
scrollbar_button_pos = [80, 10]
scrollbar_button_size = [13, 20]

scrollbar_moveable = False
scrollbar_move = 0

money = 100

# ================================================= Graphics =================================================

tileland_graphics_path = locals()
tileland_graphics = []

# === Rect ===

homebutton_rect = pygame.Rect((window_size[0]-64 - 10,10,64,64),width=0)

bar_button01_rect = pygame.Rect((10*1 + 64*0,window_size[1] - (10*1 + 64*1),64,64),width=0)
bar_button02_rect = pygame.Rect((10*2 + 64*1,window_size[1] - (10*1 + 64*1),64,64),width=0)
bar_button03_rect = pygame.Rect((10*3 + 64*2,window_size[1] - (10*1 + 64*1),64,64),width=0)
bar_button04_rect = pygame.Rect((10*4 + 64*3,window_size[1] - (10*1 + 64*1),64,64),width=0)
bar_button05_rect = pygame.Rect((10*5 + 64*4,window_size[1] - (10*1 + 64*1),64,64),width=0)

pretile_type = 0
tile_type = 0
build = False
reward = False

time_speed = 100

# === Page ===

menu_main = True
menu_stop = False
menu_setting = False
game_main = False
