
import random
import noise
import numpy

import config.data.constant as C

from panda3d.core import loadPrcFileData

loadPrcFileData('',C.config)

from direct.showbase.ShowBase import ShowBase

class MainLoop(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        # self.disableMouse()
        # self.useDrive()
        # self.useTrackball()

        world_boarder = 64
        world_hight = 16

        seed = 0
        # octaves = 2
        # freq = 12

        octaves = 10
        freq = 65

        #random.seed(random.randint(100000000, 999999999))
        seed = random.randint(100000, 999999)

        # tilemap_hight = [[[int(noise.pnoise2((x/freq)+seed,(y/freq)+seed,octaves)*100+50)] for x in range(0,world_boarder,1)] for y in range(0,world_boarder,1)]

        tilemap_hight = [[int(noise.snoise2((x/freq)+seed,(y/freq)+seed,octaves)*10+5) for x in range(0,world_boarder,1)] for y in range(0,world_boarder,1)]

        # 0 tile   1 time   2 buildable   3 Dv Code
        tilemap = [[[[0,0,0,0]for z in range(0,world_hight,1)] for x in range(0,world_boarder,1)] for y in range(0,world_boarder,1)]

        print(tilemap_hight)

        tilemap_block = numpy.zeros((world_boarder, world_boarder, world_hight), dtype = numpy.int)

        for x in range(0,world_boarder,1):
                for y in range(0,world_boarder,1):
                        for z in range(0,world_hight,1):
                                if tilemap_hight[x][y] >= 0:
                                        tilemap_block[x, y, z] = 1
                                        tilemap_hight[x][y] -= 1

        render_map = {}

        for x in range(0,world_boarder,1):
            render_map[x] = {}
            for y in range(0,world_boarder,1):
                render_map[x][y] = {}
                for z in range(0,world_hight,1):
                    if tilemap_block[x, y, z] == 1:
                        render_map[x][y][z] = self.loader.loadModel('assets/graphics/tile/tileland/tileland1.ply')
                        render_map[x][y][z].setPos(0.8*x, 0.8*y, 0.8*z)
                        render_map[x][y][z].reparentTo(self.render)
                    
                        



        # # 0 tile land   1 tile building  2 tile preview   3 time   4 buildable   5 Dv Code
        # tilemap = [[[int(noise.pnoise2((x/freq)+seed,(y/freq)+seed,octaves)*100+50),random.randint(0,100),0,0,0,0] for x in range(0,boarder,1)] for y in range(0,boarder,1)]

        # # 0 tile land render   1 tile building render  2 tile preview render
        # tilemap_tileland_render = {}
        # tilemap_tilebuilding_render = {}

        # tilemap_n = len(tilemap)
        # tilemap_m = len(tilemap[0])

        # for tilemap_x in range(tilemap_n):
        #     tilemap_tileland_render[tilemap_x] = {}
        #     tilemap_tilebuilding_render[tilemap_x] = {}

        #     for tilemap_y in range(tilemap_m):

        #         tile_info = tilemap[tilemap_x][tilemap_y]

        #         if tile_info[5] == 0:

        #         # === 0 tile_land ===

        #             if -100 <=tile_info[0]<= 37:
        #                 tile_info[0] = 4
                
        #             if 38 <=tile_info[0]<= 40:
        #                 tile_info[0] = 2
                        
        #             if 41 <=tile_info[0]<= 65:
        #                 tile_info[0] = 1
                        
        #             if 66 <=tile_info[0]<= 70:
        #                 tile_info[0] = 1 
                        
        #             if 70 <=tile_info[0]<= 110:
        #                 tile_info[0] = 3

        #         # === 1 tile_building ===

        #             if 0<=tile_info[1]<=40:
        #                 tile_info[1] = 0

        #             if 41<=tile_info[1]<=80 and tile_info[0] == 1:
        #                 tile_info[1] = 1

        #             if 81<=tile_info[1]<=90 and tile_info[0] == 1:
        #                 tile_info[1] = 2
                    
        #             if 91<=tile_info[1]<=100 and tile_info[0] == 1:
        #                 tile_info[1] = 3


        #             tile_info[5] = 1

        #         if tile_info[5] == 1:

        #             if tile_info[0] == 1:
        #                 tilemap_tileland_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tileland/tileland1.ply')
                        
        #             if tile_info[0] == 2:
        #                 tilemap_tileland_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tileland/tileland2.ply')
                        
        #             if tile_info[0] == 3:
        #                 tilemap_tileland_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tileland/tileland3.ply')
                        
        #             if tile_info[0] == 4:
        #                 tilemap_tileland_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tileland/tileland4.ply')

        #             #tilemap_tileland_render[tilemap_x][tilemap_y].setScale(64, 64, 64)
        #             tilemap_tileland_render[tilemap_x][tilemap_y].setPos(0.8*tilemap_y, 0.8*tilemap_x, 0)
        #             tilemap_tileland_render[tilemap_x][tilemap_y].reparentTo(self.render)

        #             if tile_info[1] == 1:
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tilebuilding/tilebuilding1.ply')
        #                 #tilemap_tilebuilding_render[tilemap_x][tilemap_y].setScale(64, 64, 64)
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y].setPos(0.8*tilemap_y, 0.8*tilemap_x, 0.8)
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y].reparentTo(self.render)

        #             if tile_info[1] == 2:
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tilebuilding/tilebuilding2.ply')
        #                 #tilemap_tilebuilding_render[tilemap_x][tilemap_y].setScale(64, 64, 64)
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y].setPos(0.8*tilemap_y, 0.8*tilemap_x, 0.8)
        #                 tilemap_tilebuilding_render[tilemap_x][tilemap_y].reparentTo(self.render)

        #             # if tile_info[1] == 3:
        #             #     tilemap_tilebuilding_render[tilemap_x][tilemap_y] = self.loader.loadModel('assets/graphics/tile/tilebuilding/tilebuilding2.ply')
        #             #     #tilemap_tilebuilding_render[tilemap_x][tilemap_y].setScale(64, 64, 64*4)
        #             #     tilemap_tilebuilding_render[tilemap_x][tilemap_y].setPos(0.8*tilemap_y, 0.8*tilemap_x, 0.8*3)
        #             #     tilemap_tilebuilding_render[tilemap_x][tilemap_y].reparentTo(self.render)
                        

mainloop = MainLoop()
mainloop.run()