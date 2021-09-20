
import moyu_engine.config.constants as C

def ZOOM_Fn():
    if C.ZOOM_IN == True:
        if C.GAMEmain_surface_level == 10:
            C.GAMEmain_surface_level = 10
        else:
            C.GAMEmain_surface_level -= 1
            C.MOVE[1] -= 4.25
            C.MOVE[0] -= 7.9
    if C.ZOOM_OUT == True:
        if C.GAMEmain_surface_level == 200:
            C.GAMEmain_surface_level = 200
        else:
            C.GAMEmain_surface_level += 1
            C.MOVE[1] += 4.25
            C.MOVE[0] += 7.9
    return C.GAMEmain_surface_level