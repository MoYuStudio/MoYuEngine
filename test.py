from panda3d.core import loadPrcFile
loadPrcFile('config/data/config.prc')

from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene1 = self.loader.loadModel("assets/graphics/tile/tileland/block1.obj")
        # Reparent the model to render.
        self.scene1.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene1.setScale(25, 25, 25)
        self.scene1.setPos(-8, 42, 0)

        self.scene2 = self.loader.loadModel("assets/graphics/tile/tileland/block1.obj")
        # Reparent the model to render.
        self.scene2.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene2.setScale(50, 50, 50)
        self.scene2.setPos(0, 0, 0)

app = MyApp()
app.run()