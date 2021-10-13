
import numpy
import noise

world_boarder = 16
world_hight = 5

seed = 0
# octaves = 2
# freq = 12

octaves = 10
freq = 12

tilemap_hight = [[int(noise.snoise2((x/freq)+seed,(y/freq)+seed,octaves)*10+5) for x in range(0,world_boarder,1)] for y in range(0,world_boarder,1)]

tilemap_block = numpy.zeros((world_boarder, world_boarder, world_hight), dtype = numpy.int)

for x in range(0,world_boarder,1):
        for y in range(0,world_boarder,1):
                for z in range(0,world_hight,1):
                        if tilemap_hight[x][y] >= 0:
                                tilemap_block[x, y, z] = 1
                                tilemap_hight[x][y] -= 1

print(tilemap_hight)
print(tilemap_block)
