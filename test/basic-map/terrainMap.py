from panda3d.core import StackedPerlinNoise2, PNMImage
from panda3d.core import LVector3f, LVector3i, LVector2f, LVector2i
import math
from array import *

###############################################################################
# Procedural generation of the terrain
 
def FillTerrainMapBasic(terrainRegionMap):

    trm = terrainRegionMap
    
    #Perlin Noise Base
    scale = 0.5 * 64 / trm.size
    stackedNoise = StackedPerlinNoise2(scale, scale, 8, 2, 0.5, trm.size, 0)
    terrainImage = PNMImage(trm.size, trm.size, 1)
    terrainImage.perlinNoiseFill(stackedNoise)

    #Make it look a bit more natural
    for i in range(trm.size):
        for j in range(trm.size):
            g = terrainImage.getGray(i,j)
            # make between -0.5 and 1, more land than water
            g = (g-0.25)/0.75
            # make mountain more spiky and plains more flat
            if g>0:
                g = g ** 3
            # return to 0.25 to 1 range
            g = (g+1)/2
            terrainImage.setGray(i,j,g)
    
    #Make it an island
    border = 2 * trm.size / 8
    for i in range(trm.size):
        for j in range(trm.size):
            distToEdge = min(i, trm.size-1-i, j, trm.size-1-j)
            if(distToEdge < border):
                g = terrainImage.getGray(i,j)
                g = g * math.sqrt(distToEdge / border)
                g = max(g, 0.25)
                terrainImage.setGray(i,j,g)

    # Convert to kHeight
    # Height in integer increments between -self.height and  self.height
    trm.maxKHeight = -trm.height
    for i in range(trm.size):
        for j in range(trm.size):
            kHeight= round((terrainImage.getGray(i,j)-0.5)*trm.height*2)
            trm.heightMap[i][j] = kHeight
            if(kHeight < 0):
                trm.waterMap[i][j] = True
            if(kHeight > trm.maxKHeight):
                trm.maxKHeight = kHeight

###############################################################################
# Class holding all information about a terrain region
class TerrainRegionMap:
    def __init__(self, size, height):
        
        # Dimensions and Location
        self.size = size
        self.height = height
        self.cellDimension = 2.0
        self.heightStep = 0.5
        self.center = LVector2f(0.0, 0.0)

        # Memory space for terrain data
        self.heightMap = [[0 for i in range(self.size)] for j in range(self.size)]
        self.waterMap = [[False for i in range(self.size)] for j in range(self.size)]
        self.waterOffset = self.heightStep / 2.0

        # Statistics for the terrain data
        self.maxKHeight = 0.0
    
    def isValid(self, i,j):
        return i >= 0 and i < self.size and j >= 0 and j < self.size
    
    def hasWater(self, i, j):
        return self.waterMap[i][j] == True
    
    def getKHeightFromZ(self, z):
        return round(z/self.heightStep)

    def getZHeightFromK(self, k):
        return k * self.heightStep
    
    def getKHeightFromIJ(self, i, j):
        return self.heightMap[i][j]

    def getZHeightFromIJ(self, i, j):
        return self.getZHeightFromK(self.getKHeightFromIJ(i,j)) 

    def getZHeightFromXY(self, x, y):
        ijLocation = self.getIJLocationFromXY(LVector2f(x,y))
        return self.getZHeightFromIJ(ijLocation.getX(), ijLocation.getY())

    def getIJLocationFromXY(self, XYLocation):
        return LVector2i(
            round((XYLocation.getX()+self.size)/2),
            round((XYLocation.getY()+self.size)/2))

    def getXYLocationFromIJ(self, IJLocation):
        return LVector2f(
            2*IJLocation.getX()-self.size, 
            2*IJLocation.getY()-self.size)