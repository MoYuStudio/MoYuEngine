from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import lookAt
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import CollideMask
from panda3d.core import Texture, GeomNode, TransparencyAttrib
from panda3d.core import PerspectiveLens
from panda3d.core import CardMaker
from panda3d.core import Light, DirectionalLight, AmbientLight
from panda3d.core import TextNode
from panda3d.core import LVector3
from panda3d.core import NodePath
from panda3d.core import Fog

from panda3d.core import Material

import sys
import os

import cProfile

from navigation import *
from terrainMesh import TerrainMesher
from avatar import LightworldAvatarControler 

# Function to put text on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.04,
                        shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                        pos=(0.08, -pos - 0.04), align=TextNode.ALeft)

def addStatistics(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.04,
                        shadow=(0, 0, 0, 1), parent=base.a2dBottomLeft,
                        pos=(0.08, pos + 0.04), align=TextNode.ALeft)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), scale=.06,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        pos=(-0.1, 0.09), shadow=(0, 0, 0, 1))

# Game Class
class LightworldBasic(ShowBase):
    def __init__(self):
        
        # Interactive or overview mode
        self.overview = True

        # Set up the window, camera, etc.
        ShowBase.__init__(self)

        # Set the background color to blue
        self.skyBackgroundColor = (0.4, 0.7, 1.0)
        self.seaBackgroundColor = (0.16, 0.72, 0.87)
        self.setBackgroundColor(*self.skyBackgroundColor)
               
        # Post the instructions
        self.title = addTitle("Lightworld: Explore the map")       
        self.inst =[]
        self.inst.append(addInstructions(0.05, "[ESC]: Quit"))
        self.inst.append(addInstructions(0.10, "[v]: Toggle Overview"))
        self.inst.append(addInstructions(0.15, "[+/-]: Change Size and Recreate"))
        self.inst.append(addInstructions(0.20, "[Space]: Update Terrain"))
        self.inst.append(addInstructions(0.25, "[Left Arrow]: Rotate Left"))
        self.inst.append(addInstructions(0.30, "[Right Arrow]: Rotate Right"))
        self.inst.append(addInstructions(0.35, "[Up Arrow]: Move Forward"))
        self.inst.append(addInstructions(0.40, "[Down Arrow]: Move Backward"))


        self.terrainSize = 64
        self.terrainHeight = 18
        self.stat = []
        self.terrainSizeMsg = "Terrain Size: {0}"
        self.stat.append(addStatistics(0.10, self.terrainSizeMsg.format(self.terrainSize)))
        self.terrainMaxHeightMsg = "Terrain Max Height: {0}"
        self.stat.append(addStatistics(0.05, self.terrainMaxHeightMsg.format(self.terrainHeight)))

        # Create the avatar
        avatarHeight = 1.6
        cameraDistance = 1
        self.avatarControler = LightworldAvatarControler(avatarHeight, cameraDistance)
        
        self.linfog = Fog("A linear-mode Fog node")
        self.linfog.setColor(0.16, 0.72, 0.87)
        self.linfog.setLinearRange(0,18)
        self.linfog.setLinearFallback(45,6,18)
        self.camera.attachNewNode(self.linfog)
        render.setFog(self.linfog)

        # Initialize terrain and avatar
        self.texture = loader.loadTexture("terrainTex2.png") 
        self.terrainNode = NodePath()
        self.waterNode = NodePath()
        self.terrainMesher = TerrainMesher() 

        # Generate terrain and position avatar
        self.updateTerrain()

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        self.accept("v", self.toggleOverview)
        self.accept("+", self.increaseTerrainSize)
        self.accept("-", self.decreaseTerrainSize)
        self.accept("space", self.updateTerrain)
        self.accept("arrow_left", self.turnLeft)
        self.accept("arrow_right", self.turnRight)
        self.accept("arrow_up", self.moveForward)
        self.accept("arrow_down", self.moveBackward)
        taskMgr.add(self.move, "moveTask")

        self.disableMouse()
        self.toggleOverview()

        # Create some lighting
        alight = AmbientLight('alight')
        alight.setColor((0.2, 0.2, 0.2, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)

        dlight2 = DirectionalLight('dlight2')
        dlight2.setColor((0.1, 0.1, 0.1, 1))
        dlnp2 = render.attachNewNode(dlight2)
        render.setLight(dlnp2)
        dlnp2.setHpr(20, -5, 0)
        
        dlight3 = DirectionalLight('dlight3')
        dlight3.setColor((0.6, 0.6, 0.6, 1))
        dlnp3 = render.attachNewNode(dlight3)
        render.setLight(dlnp3)
        dlnp3.setHpr(-100, -50, 0)
        
    def updateAvatarPosition(self):
        self.avatarControler.setInitialPos(0,0,self.terrainMesher.heightMap.getZHeightFromXY(0.0,0.0))
    
    def updateCameraPosition(self):
        if self.overview == False:
            self.camera.setPos(self.avatarControler.curCamPos)
            self.camera.lookAt(self.avatarControler.curPos)
            if(not render.hasFog() and self.camera.getPos().getZ() < -0.25):
                render.setFog(self.linfog)
                self.setBackgroundColor(*self.seaBackgroundColor)
            elif(render.hasFog() and self.camera.getPos().getZ() > -0.25):
                render.clearFog()
                self.setBackgroundColor(*self.skyBackgroundColor)
        else:
            self.camera.setPos(LVector3(-2.2 * self.terrainSize, -1.7 * self.terrainSize, self.terrainSize) )
            self.camera.lookAt(LVector3(-0.1 * self.terrainSize, 0.0, -0.30 * self.terrainSize))
            if(render.hasFog()):
                render.clearFog()
                self.setBackgroundColor(*self.skyBackgroundColor)

    def updateTerrain(self):
        self.terrainMesher.generateTerrain(self.terrainSize, self.terrainHeight)
        self.updateTerrainMesh()
        self.updateWaterMesh()
        self.updateAvatarPosition()
        self.updateCameraPosition()
        self.stat[0].setText(self.terrainSizeMsg.format(self.terrainSize))
        self.stat[1].setText(self.terrainMaxHeightMsg.format(self.terrainHeight))

    def updateTerrainMesh(self):
        self.terrainNode.removeNode()
        terrainMesh = self.terrainMesher.meshTerrain()
        snode = GeomNode('terrainPatch')
        snode.addGeom(terrainMesh)
        self.terrainNode = render.attachNewNode(snode)
        self.terrainNode.setTexture(self.texture)

    def updateWaterMesh(self):
        self.waterNode.removeNode()
        waterMesh = self.terrainMesher.meshWater()
        snode = GeomNode('waterPatch')
        snode.addGeom(waterMesh)
        self.waterNode = render.attachNewNode(snode)
        self.waterNode.setTexture(self.texture)
        self.waterNode.setTwoSided(True)
        self.waterNode.setTransparency(TransparencyAttrib.M_alpha)

    def increaseTerrainSize(self):
        self.terrainSize = round(self.terrainSize * 2.0)
        self.terrainHeight = round(self.terrainHeight * 1.5)
        self.updateTerrain()

    def decreaseTerrainSize(self):
        if(self.terrainSize > 1):
            self.terrainSize = round(self.terrainSize / 2.0)
            self.terrainHeight = round(self.terrainHeight / 1.5)
            self.updateTerrain()

    def toggleOverview(self):
        self.overview = not self.overview
        if self.overview == False:
            self.camLens.setFocalLength(0.4)
            self.camLens.setNear(0.1)          
            self.inst[4].show()
            self.inst[5].show()
            self.inst[6].show()
            self.inst[7].show()
        else:
            self.disableMouse()
            self.camLens.setFocalLength(1)
            self.inst[4].hide()
            self.inst[5].hide()
            self.inst[6].hide()
            self.inst[7].hide()
            
        self.updateCameraPosition()

    def moveForward(self):
        if self.overview == False:
            target = self.avatarControler.getTargetForwardCell()
            target.setZ(self.terrainMesher.heightMap.getZHeightFromXY(target.getX(),target.getY()))
            self.avatarControler.triggerMove(target)

    def moveBackward(self):
        if self.overview == False:
            target = self.avatarControler.getTargetBackwardCell()
            target.setZ(self.terrainMesher.heightMap.getZHeightFromXY(target.getX(),target.getY()))
            self.avatarControler.triggerMove(target)

    def turnLeft(self):
        if self.overview == False:
            self.avatarControler.triggerTurnLeft()
    
    def turnRight(self):
        if self.overview == False:
            self.avatarControler.triggerTurnRight()

    def move(self, task):       
        if(self.avatarControler.moving == True):
            self.avatarControler.moveByDistance(0.15)
            self.camera.setPos(self.avatarControler.curCamPos)
            self.camera.lookAt(self.avatarControler.curPos)
        elif(self.avatarControler.turning == True):
            self.avatarControler.turnByDistance(0.15)
            self.camera.setPos(self.avatarControler.curCamPos)
            self.camera.lookAt(self.avatarControler.curPos)
        if(self.overview == False):
            if(not render.hasFog() and self.camera.getPos().getZ() < -0.25):
                render.setFog(self.linfog)
                self.setBackgroundColor(*self.seaBackgroundColor)
            elif(render.hasFog() and self.camera.getPos().getZ() > -0.25):
                render.clearFog()
                self.setBackgroundColor(*self.skyBackgroundColor)
        return task.cont

demo = LightworldBasic()
demo.run()
