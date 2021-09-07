
'''
import sys
import noise
import random
random.seed()
octaves = random.random()
freq = 16.0 * octaves
for y in range(30):
    for x in range(40):
        n = int(noise.pnoise2(x/freq, y / freq, 1)*10+3)
        print(n)
'''

import sys
import noise
import random

print(random.seed())
octaves = 2
freq = 10

boarder = 8

tilemap = [[[(noise.pnoise2(x/freq, y / freq, octaves)*3)] for x in range(0,boarder,1)] for y in range(0,boarder,1)]

print(tilemap)