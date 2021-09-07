
import pickle

import moyu_engine.config.constants as C

def read_tilemap():

    f=open('moyu_engine/config/data/game_save', 'rb')

    data = pickle.load(f)

    C.tilemap = data['map']

    f.close()


"""
import os

import moyu_engine.config.constants as C

def read_tilemap():

    f=open('moyu_engine/config/data/tilemap','r')

    read_str = f.read()

    C.tilemap = read_str.split('#')

    f.close()

def read_test():

    f=open('moyu_engine/config/data/tilemap','r')

    test_tilemap = f.read()
    print(test_tilemap)

    f.close()
"""