
import pickle

import moyu_engine.config.constants as C

def save_tilemap():

    f=open('moyu_engine/config/data/game_save','wb')

    save_data = {'map':C.tilemap}

    pickle.dump(save_data, f)

    f.close()

"""
import os

import moyu_engine.config.constants as C

def save_tilemap():

    f=open('moyu_engine/config/data/tilemap','w')

    tilemap_n = len(C.tilemap)
    tilemap_m = len(C.tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = C.tilemap[tilemap_x][tilemap_y]

            save_str = '#'.join(str(i)for i in tile_info)
            f.write(save_str)

        save_str = '@'.join(str(j)for j in tilemap_m)
        f.write(save_str)

    f.write(save_str)

    f.close()
"""