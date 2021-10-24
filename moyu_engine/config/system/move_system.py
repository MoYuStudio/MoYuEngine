
import config.data.constants as C

class MoveSystem:

    @ staticmethod
    def move():
        if C.window['move_switch']['up'] == True:
            C.window['move_y'] += C.window['move_speed']
        if C.window['move_switch']['down'] == True:
            C.window['move_y'] -= C.window['move_speed']
        if C.window['move_switch']['left'] == True:
            C.window['move_x'] -= C.window['move_speed']
        if C.window['move_switch']['right'] == True:
            C.window['move_x'] += C.window['move_speed']

    @ staticmethod
    def zoom():
        if C.window['zoom_switch']['in'] == True:
            if C.window['surface_level'] <= 0.25:
                C.window['surface_level'] = 0.25
            else:
                C.window['surface_level'] -= 0.025
                C.window['move'][1] -= 4.25
                C.window['move'][0] -= 7.9
        if C.window['zoom_switch']['out'] == True:
            if C.window['surface_level'] >= 1:
                C.window['surface_level'] = 1
            else:
                C.window['surface_level'] += 0.025
                C.window['move'][1] += 4.25
                C.window['move'][0] += 7.9