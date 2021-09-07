
import os

import moyu_engine.config.constants as C

def save_tilemap():

    f=open('moyu_engine/config/data/tilemap','w')

    f.write(str(C.tilemap))

    f.close()
