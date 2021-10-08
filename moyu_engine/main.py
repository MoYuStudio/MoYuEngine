
import random
import noise

import config.data.constant as C

from panda3d.core import loadPrcFileData

loadPrcFileData('',C.config)

from direct.showbase.ShowBase import ShowBase

class MainLoop(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        # self.disableMouse()

        board = 8
        
        tilemap = [[random.randint(0,1) for x in range(0,board,1)] for y in range(0,board,1)]

        print(tilemap)

        tilemap_render = {}
        for i in range(0,board,1):
            tilemap_render[i] = {}
            for j in range(0,board,1):

                if tilemap[i][j] == 0:
                    tilemap_render[i][j] = self.loader.loadModel('assets/graphics/tile/tileland/tileland1.ply')
                if tilemap[i][j] == 1:
                    tilemap_render[i][j] = self.loader.loadModel('assets/graphics/tile/tileland/tileland4.ply')

                tilemap_render[i][j].setScale(64, 64, 64)
                tilemap_render[i][j].setPos(8*6.4*j, 8*6.4*i, 0)
                tilemap_render[i][j].reparentTo(self.render)

mainloop = MainLoop()
mainloop.run()