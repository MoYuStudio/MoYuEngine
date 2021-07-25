
import random

boarder = 16

def tilemap_builder():
    global tilemap

    # 0 tile land   1 tile   2 country   3 army   4 time   5 buildable   6 tile button x   7 tile button y   8 Dv Code

    tilemap = [[[random.randint(0,600),random.randint(0,100),0,random.randint(0,100),0,0,0,0,0] for i in range(0,boarder,1)] for j in range(0,boarder,1)]

    print(tilemap)
    return tilemap

tilemap_builder()