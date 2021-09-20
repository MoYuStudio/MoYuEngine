
import pygame

# =============================================== =  = Window =============================================== =  = 

WINDOW_SIZE = [1280,720]

SCREEN       = pygame.display.set_mode(WINDOW_SIZE)
SCREEN_TITLE = pygame.display.set_caption('Tinyland 弹丸之地')

# Window Page =============================================== =  = 

MENUmain      = True
MENUstop      = False
MENUsetting   = False
MENUcreatemap = False
GAMEmain      = False

# =============================================== =  = MOVE =============================================== =  = 

MOVE       = [0,0]
MOVE_SPEED = 10

MOVE_UP    = False
MOVE_DOWN  = False
MOVE_LEFT  = False
MOVE_RIGHT = False

# =============================================== =  = ZOOM =============================================== =  = 

ZOOM_IN  = False
ZOOM_OUT = False

# =============================================== =  = CLOCK =============================================== =  = 

CLOCK = pygame.time.Clock()

# =============================================== =  = TILE =============================================== =  = 

boarder   = 64
tile_size = 64

tile_choose      = False
tile_choose_info = [0,0,0]

tile_choose_info = [0,0,0,0,0,0]

tilemap = []

money = 100

#mouse_x,mouse_y = (boarder/2*(tile_size/2)-boarder/2*(tile_size/2)), (boarder/2*(tile_size/4)+boarder/2*(tile_size/4))

mouse_pos_x      ,                 mouse_pos_y = 0, 0
mouse_down_pos_x,mouse_down_pos_y = 0,          0

# =============================================== =  = Surface =============================================== =  = 

tilemap_surface_level = 60

tilemap_surface_size = [16*tilemap_surface_level,9*tilemap_surface_level]
tilemap_surface     = pygame.Surface(tilemap_surface_size).convert_alpha()

surface_level = (1280/(16*tilemap_surface_level))

# GAME main surface =============================================== =  = 

GAMEmain_surface_level = 60

# 320 180 n = 20        16*n  9*n    1280 720 n = 80

GAMEmain_surface_size = [16*GAMEmain_surface_level,9*GAMEmain_surface_level]
GAMEmain_surface      = pygame.Surface(GAMEmain_surface_size)

#surface_level = (1280/(16*GAMEmain_surface_level))

# GAME main gui surface =============================================== =  = 

GAMEmain_gui_surface_level = 80

# 320 180 n = 20        16*n  9*n    1280 720 n = 80

GAMEmain_gui_surface_size = [16*GAMEmain_gui_surface_level,9*GAMEmain_gui_surface_level]
GAMEmain_gui_surface      = pygame.Surface(GAMEmain_gui_surface_size)

#surface_level = (1280/(16*GAMEmain_gui_surface_level))

# MENU main surface =============================================== =  = 

MENUmain_surface_level = 80

# 320 180 n = 20        16*n  9*n    1280 720 n = 80

MENUmain_surface_size = [16*MENUmain_surface_level,9*MENUmain_surface_level]
MENUmain_surface      = pygame.Surface(MENUmain_surface_size)

# fade_black surface =============================================== =  = 

fade_black_surface_size = WINDOW_SIZE
fade_black_surface      = pygame.Surface(fade_black_surface_size)

# =============================================== =  = Scrollbar =============================================== =  = 

scrollbar_line_color = [255, 255, 255]
scrollbar_line_pos   = [85, 10]
scrollbar_line_size  = [3, 360]

scrollbar_button_color = [161, 136, 127]
scrollbar_button_pos   = [80, 10]
scrollbar_button_size  = [13, 20]

scrollbar_moveable = False
scrollbar_move     = 0

# =============================================== =  = Graphics =============================================== =  = 

tileland_graphics_path = locals()
tileland_graphics      = []

# =============================================== =  = Rect =============================================== =  = 

homebutton_RECT = pygame.Rect((WINDOW_SIZE[0]-64 - 10,10,64,64),width=0)

GAMEbar_button01_RECT = pygame.Rect((10*1 + 64*0,WINDOW_SIZE[1] - (10*1 + 64*1),64,64),width=0)
GAMEbar_button02_RECT = pygame.Rect((10*2 + 64*1,WINDOW_SIZE[1] - (10*1 + 64*1),64,64),width=0)
GAMEbar_button03_RECT = pygame.Rect((10*3 + 64*2,WINDOW_SIZE[1] - (10*1 + 64*1),64,64),width=0)
GAMEbar_button04_RECT = pygame.Rect((10*4 + 64*3,WINDOW_SIZE[1] - (10*1 + 64*1),64,64),width=0)
GAMEbar_button05_RECT = pygame.Rect((10*5 + 64*4,WINDOW_SIZE[1] - (10*1 + 64*1),64,64),width=0)

MENUmain_button01_RECT = pygame.Rect((WINDOW_SIZE[0]-64*3*1 - 20, WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
MENUmain_button02_RECT = pygame.Rect((WINDOW_SIZE[0]-64*3*1 - 20, WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
MENUmain_button03_RECT = pygame.Rect((WINDOW_SIZE[0]-64*3*1 - 20, WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
MENUmain_button04_RECT = pygame.Rect((WINDOW_SIZE[0]-64*3*1 - 20, WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
MENUmain_button05_RECT = pygame.Rect((WINDOW_SIZE[0]-64*3*1 - 20, WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

pretile_type = 0
tile_type    = 0
build        = False
reward       = False

time_speed = 100


# =============================================== =  = Perlin Noise =============================================== =  = 

octaves = 2
freq    = 12

seed = 0

# =============================================== =  = fade_black =============================================== =  = 

fade_black       = False
fade_black_alpha = 0
window_switch    = False

buttonStartGame     = False
button_ContinueGame = False