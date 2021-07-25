
import random

import test2

def tilemap_builder():

    tilemap = [[[random.randint(0,600),random.randint(0,100),0,0,0,0,0] for i in range(0,3,1)] for j in range(0,3,1)]

    test2.tilemap = tilemap

    return tilemap