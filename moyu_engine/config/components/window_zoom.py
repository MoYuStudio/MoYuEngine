
import moyu_engine.config.constants as C

def zoom_Fn():
    if C.zoom_in == True:
        if C.GAMEmain_surface_level == 10:
            C.GAMEmain_surface_level = 10
        else:
            C.GAMEmain_surface_level -= 1
            C.move_y -= 4.25
            C.move_x -= 7.9
    if C.zoom_out == True:
        if C.GAMEmain_surface_level == 200:
            C.GAMEmain_surface_level = 200
        else:
            C.GAMEmain_surface_level += 1
            C.move_y += 4.25
            C.move_x += 7.9
    return C.GAMEmain_surface_level