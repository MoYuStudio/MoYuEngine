
import data.constants as C

class MoveSystem:

    def MOVE_Fn():
        if C.MOVE_UP == True:
            C.MOVE[1] += C.MOVE_SPEED
        if C.MOVE_DOWN == True:
            C.MOVE[1] -= C.MOVE_SPEED
        if C.MOVE_LEFT == True:
            C.MOVE[0] += C.MOVE_SPEED
        if C.MOVE_RIGHT == True:
            C.MOVE[0] -= C.MOVE_SPEED
        return C.MOVE[0],C.MOVE[1],C.MOVE_UP,C.MOVE_DOWN,C.MOVE_LEFT,C.MOVE_RIGHT

    def ZOOM_Fn():
        if C.ZOOM_IN == True:
            if C.tilemap_surface_level == 10:
                C.tilemap_surface_level = 10
            else:
                C.tilemap_surface_level -= 1
                C.MOVE[1] -= 4.25
                C.MOVE[0] -= 7.9
        if C.ZOOM_OUT == True:
            if C.tilemap_surface_level == 200:
                C.tilemap_surface_level = 200
            else:
                C.tilemap_surface_level += 1
                C.MOVE[1] += 4.25
                C.MOVE[0] += 7.9
        return C.tilemap_surface_level