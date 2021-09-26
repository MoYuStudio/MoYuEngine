
import data.constants as C

class MoveSystem:

    @ staticmethod
    def move():
        if C.window['move_switch']['up'] == True:
            C.window['move'][1] += C.window['move_speed']
        if C.window['move_switch']['down'] == True:
            C.window['move'][1] -= C.window['move_speed']
        if C.window['move_switch']['left'] == True:
            C.window['move'][0] += C.window['move_speed']
        if C.window['move_switch']['right'] == True:
            C.window['move'][0] -= C.window['move_speed']

    @ staticmethod
    def zoom():
        if C.window['zoom_switch']['in'] == True:
            if C.tilemap_surface_level == 10:
                C.tilemap_surface_level = 10
            else:
                C.tilemap_surface_level -= 1
                C.MOVE[1] -= 4.25
                C.MOVE[0] -= 7.9
        if C.window['zoom_switch']['out'] == True:
            if C.tilemap_surface_level == 200:
                C.tilemap_surface_level = 200
            else:
                C.tilemap_surface_level += 1
                C.MOVE[1] += 4.25
                C.MOVE[0] += 7.9