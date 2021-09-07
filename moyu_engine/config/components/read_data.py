
import pickle

import moyu_engine.config.constants as C

def read_tilemap():

    f1 = open('moyu_engine/config/data/tilemap', 'rb')

    data1 = pickle.load(f1)

    C.tilemap = data1['map']

    print(data1)



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