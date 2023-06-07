
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import random

import noise

class NoiseMap:
    def __init__(self, size = 32):
        self.size = size
        
        self.noise_map = [[0.0] * self.size for _ in range(self.size)]
        self.octaves = 2
        self.freq = random.randint(12, 16)
        self.seed = random.randint(100000, 999999)
    
    def berlin_noise(self):
        
        for y in range(self.size):
            for x in range(self.size):
                self.noise_map[y][x] = int(noise.pnoise2((x / self.freq) + self.seed, (y / self.freq) + self.seed, self.octaves) * 100 + 50)

        return self.noise_map
    
if __name__ == '__main__':
    pass
