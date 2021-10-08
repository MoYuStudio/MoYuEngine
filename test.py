
import config.data.constant as C

from panda3d.core import loadPrcFileData

loadPrcFileData('',C.config)

from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        # self.disableMouse()

        self.scene1 = self.loader.loadModel("assets/graphics/tile/tileland/block1.obj")
        self.scene1.reparentTo(self.render)
        self.scene1.setScale(64, 64, 64)
        self.scene1.setPos(7, 0, 0)#6

        self.scene1.reparentTo(self.render)
        self.scene1.setScale(64, 64, 64)
        self.scene1.setPos(14, 7, 0)#6

        self.scene2 = self.loader.loadModel("assets/graphics/tile/tileland/block1.obj")
        self.scene2.reparentTo(self.render)
        self.scene2.setScale(64, 64, 64)
        self.scene2.setPos(0, 0, 0)

app = MyApp()
app.run()