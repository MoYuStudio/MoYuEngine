import os

import moyu_engine.config.constants as C

def read_tilemap():

    f=open('moyu_engine/config/data/tilemap','r')

    C.tilemap = f.read()

    f.close()

def read_test():

    f=open('moyu_engine/config/data/tilemap','r')

    test_tilemap = f.read()
    print(test_tilemap)

    f.close()
