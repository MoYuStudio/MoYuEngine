
import constants as C

def zoom_Fn():
    if C.zoom_in == True:
        if C.game_main_surface_level == 10:
            C.game_main_surface_level = 10
        else:
            C.game_main_surface_level -= 1
    if C.zoom_out == True:
        if C.game_main_surface_level == 60:
            C.game_main_surface_level = 60
        else:
            C.game_main_surface_level += 1
    return C.game_main_surface_level