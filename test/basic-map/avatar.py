from panda3d.core import LVector3
from navigation import *

# Description
# Playable avatar

class LightworldAvatarControler:
    
    def __init__(self, height, camDist):
        # Avatar and Cam Positions
        self.avatarHeight = height
        self.camDist = camDist
        
        # Current Position
        self.curPos = LVector3(0,0,0)
        self.curHeading = "yp"
        #self.curMoveDir = LVector3(0,1,0)
        self.curCamPos = self.curPos - self.getMoveDir() * self.camDist

        # Target position for next move
        self.targetPos = self.curPos
        self.targetMoveHeading = self.curHeading
        self.targetCamPos = self.curCamPos

        #State
        self.canReceiveCommand = True
        self.moving = False
        self.turning = False
    
    def setInitialPos(self, x, y, terrainHeight):
         self.curPos = LVector3(x,y, terrainHeight + self.avatarHeight)
         self.curCamPos = self.curPos - self.getMoveDir() * self.camDist

    def getMoveDir(self):
        return Heading.getDirection3f(self.curHeading)
    
    def getTargetForwardCell(self):
        return self.curPos + Heading.getDirection3f(self.curHeading) * Heading.getNextCellDist(self.curHeading)

    def getTargetBackwardCell(self):
        backHeading = Heading.getDirection3f(Heading.getOpposite(self.curHeading))
        return self.curPos + backHeading * Heading.getNextCellDist(self.curHeading)

    def triggerMove(self, target):
        if(self.canReceiveCommand):
            self.moving = True
            self.canReceiveCommand = False
            self.targetPos = target
            self.targetPos.setZ(self.targetPos.getZ()+self.avatarHeight)
    
    def moveByDistance(self, distanceToMove):
        if(self.moving):
            distanceToTarget = (self.targetPos-self.curPos).length()
            if(distanceToTarget<distanceToMove):
                self.curPos = self.targetPos
                self.moving = False
                self.canReceiveCommand = True
            else:
                dir = (self.targetPos-self.curPos) * (1/distanceToTarget)
                newPos = self.curPos + dir * distanceToMove
                self.curPos = newPos
            self.curCamPos = self.curPos - self.getMoveDir() * self.camDist

    def triggerTurnLeft(self):
        if(self.canReceiveCommand):
            self.turning = True
            self.canReceiveCommand = False
            self.targetMoveHeading = Heading.getLeft45(self.curHeading)
            self.targetCamPos = self.curPos - Heading.getDirection3f(self.targetMoveHeading) * self.camDist

    def triggerTurnRight(self):
        if(self.canReceiveCommand):
            self.turning = True
            self.canReceiveCommand = False
            self.targetMoveHeading = Heading.getRight45(self.curHeading)
            self.targetCamPos = self.curPos - Heading.getDirection3f(self.targetMoveHeading) * self.camDist

    def turnByDistance(self, distanceToMove):
        if(self.turning):
            distanceToTarget = (self.targetCamPos-self.curCamPos).length()
            if(distanceToTarget<distanceToMove):
                self.curCamPos = self.targetCamPos
                self.curHeading = self.targetMoveHeading
                self.turning = False
                self.canReceiveCommand = True
            else:
                dir = (self.targetCamPos-self.curCamPos) * (1/distanceToTarget)
                newPos = self.curCamPos + dir * distanceToMove
                self.curCamPos = newPos

    