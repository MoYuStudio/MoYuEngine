
import moyu_engine.config.constants as C

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