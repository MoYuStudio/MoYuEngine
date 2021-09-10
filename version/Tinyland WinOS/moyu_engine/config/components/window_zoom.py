
import moyu_engine.config.constants as C

def zoom_Fn():
    if C.zoom_in == True:
        if C.game_main_surface_level == 10:
            C.game_main_surface_level = 10
        else:
            C.game_main_surface_level -= 1
            C.move_y -= 4.25
            C.move_x -= 7.9
    if C.zoom_out == True:
        if C.game_main_surface_level == 100:
            C.game_main_surface_level = 100
        else:
            C.game_main_surface_level += 1
            C.move_y += 4.25
            C.move_x += 7.9
    return C.game_main_surface_level