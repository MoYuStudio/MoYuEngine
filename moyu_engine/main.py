
import random
import noise
import numpy
import panda3d

import config.data.constant as C

from panda3d.core import loadPrcFileData
from panda3d.core import Fog
from panda3d.core import PointLight
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight
from panda3d.core import GeoMipTerrain

loadPrcFileData('',C.config)

from direct.showbase.ShowBase import ShowBase



class MainLoop(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        # self.skyBackgroundColor = (0.4, 0.7, 1.0)
        # self.seaBackgroundColor = (0.16, 0.72, 0.87)
        # self.setBackgroundColor(*self.skyBackgroundColor)

        # self.linfog = Fog("A linear-mode Fog node")
        # self.linfog.setColor(0.16, 0.72, 0.87)
        # self.linfog.setLinearRange(0,18)
        # self.linfog.setLinearFallback(45,6,18)
        # self.camera.attachNewNode(self.linfog)
        # render.setFog(self.linfog)

        a = self.loader.loadModel('assets/graphics/tile/tileland/tileland1.glb')
        a.setPos(0, 0, 0)
        a.reparentTo(self.render)

        terrain = GeoMipTerrain("mySimpleTerrain")
        terrain.setHeightfield("yourHeightField.png")
        #terrain.setBruteforce(True)
        terrain.getRoot().reparentTo(render)
        terrain.generate()

        self.cam.setPos(5,-50,10)

mainloop = MainLoop()
mainloop.run()