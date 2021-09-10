
import moyu_engine.config.constants as C

def move_Fn():
    if C.move_up == True:
        C.move_y += C.move_speed
    if C.move_down == True:
        C.move_y -= C.move_speed
    if C.move_left == True:
        C.move_x += C.move_speed
    if C.move_right == True:
        C.move_x -= C.move_speed
    return C.move_x,C.move_y,C.move_up,C.move_down,C.move_left,C.move_right