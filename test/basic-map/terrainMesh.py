import random
import math

from terrainMap import *
from navigation import *
from meshing import *

###############################################################################
# Class managing texture computation

class TerrainTextureScheme:

    def __init__(self):
        self.uvMap = TextureUVMap(4)
        self.uvMap.addMaterial("rock", 0, 0)
        self.uvMap.addMaterial("snow", 1, 0)
        self.uvMap.addMaterial("dirt", 2, 0)
        self.uvMap.addMaterial("hillgrass", 0, 1)
        self.uvMap.addMaterial("plaingrass", 1, 1)
        self.uvMap.addMaterial("darksand", 2, 1)
        self.uvMap.addMaterial("lightsand", 3, 1)
        self.uvMap.addMaterial("darkwater", 0, 2)
        self.uvMap.addMaterial("clearwater", 1, 2)

    def getMaterial(self, zHeight, maxHeight, normal):
        zPercent = zHeight / maxHeight
        if(zPercent<-0.101):
            return "darksand"
        if(zPercent<-0.001):
            return "lightsand"
        elif(zPercent<0.021):
            return "plaingrass"
        elif(zPercent<0.401):
            return "hillgrass"
        elif(zPercent<0.701):
            return "rock"
        else:
            return "snow"

###############################################################################
# Cell shape class refactored
class CellShape2:

    def __init__(self):
        pass

    def getWaterFaces(self, center):
        fList = []
        waterCenter = center
        fList.append(CellFace.MakeSquareFace(
            waterCenter, 
            LVector3f(0.0, 0.0, 1.0), 
            LVector3f(0.0, 1.0, 0.0), 
            1.0, 1.0, 1.0))
        return fList
    
    def getFaces(self, cellMeshInfo):
        cmi = cellMeshInfo
        fList = []
        fList.append(CellFace.MakeSquareFace(
            cmi.center, 
            LVector3f(0.0, 0.0, 1.0), 
            LVector3f(0.0, 1.0, 0.0), 
            cmi.centerComp.radius, cmi.centerComp.radius, 
            1.0))

        midRadius = (cmi.radius+cmi.centerComp.radius) / 2.0
        ringHalfWitdh = (cmi.radius-cmi.centerComp.radius) / 2.0
        ringHalfWitdhDiag = (cmi.radius-cmi.centerComp.radius) / 2.0 * math.sqrt(2.0)
        for sc in cmi.sideCompList:
            headingDir = Heading.getDirection3f(sc.heading)
            center = cmi.center + headingDir * midRadius
            if(sc.slope == "flat"):
                fList.append(CellFace.MakeSquareFace(
                    center, 
                    LVector3f(0.0, 0.0, 1.0), 
                    headingDir,
                    cmi.centerComp.radius,
                    ringHalfWitdh,
                    1.0))                
            elif(sc.slope == "tapered"):
                tcenter = center + LVector3f(0.0, 0.0, 1.0) * cmi.stepHeight / 2.0
                tnormal = (LVector3f(0.0, 0.0, 1.0) - headingDir)
                tnormal.normalize()
                tup = (headingDir + LVector3f(0.0, 0.0, 1.0))
                tup.normalize()
                fList.append(CellFace.MakeSquareFace(
                    tcenter, 
                    tnormal, 
                    tup,
                    cmi.centerComp.radius,
                    ringHalfWitdhDiag,
                    1.0)) 
                
                # Vertical for further rise
                for lvl in range(1,sc.rise):
                    vcenter = cmi.center + headingDir * cmi.radius + LVector3f(0.0, 0.0, 1.0) * cmi.stepHeight * (2.0 * lvl + 1.0) / 2.0
                    vnormal = -headingDir
                    vup = LVector3f(0.0, 0.0, 1.0)
                    fList.append(CellFace.MakeSquareFace(
                        vcenter, 
                        vnormal, 
                        vup,
                        cmi.radius,
                        ringHalfWitdh,
                        1.0))
                
        for cc in cmi.cornerCompList:
            headingDir = Heading.getDirection3f(cc.heading)
            center = cmi.center + headingDir * midRadius
            if(cc.slope == "flat"):
                fList.append(CellFace.MakeSquareFace(
                    center, 
                    LVector3f(0.0, 0.0, 1.0), 
                    LVector3f(0.0, 1.0, 0.0),
                    ringHalfWitdh,
                    ringHalfWitdh,
                    1.0))
            
            elif(cc.slope == "taperedxn" or cc.slope == "taperedyn" or cc.slope == "taperedxp" or cc.slope == "taperedyp"):
                taperHeading = cc.slope[-2:]
                taperHeadingDir = Heading.getDirection3f(taperHeading)
                taperAxis = Heading.getAxis(taperHeading)
                center = center + LVector3f(0.0, 0.0, 1.0) * cmi.stepHeight / 2.0
                normal = (LVector3f(0.0, 0.0, 1.0) - taperHeadingDir)
                normal.normalize()
                up = (taperHeadingDir + LVector3f(0.0, 0.0, 1.0))
                up.normalize()
                fList.append(CellFace.MakeSquareFace(
                    center, 
                    normal, 
                    up,
                    ringHalfWitdh,
                    ringHalfWitdhDiag,
                    1.0))         

                # Need to fill side triangle in case cell in non-taper dir is lower
                adjHeadings = Heading.getAdjascentHeadings(cc.heading)
                for h in adjHeadings:
                    if not(h == taperHeading):
                        nonTaperHeading = h
                nonTaperHeadingDir = Heading.getDirection3f(nonTaperHeading)
                nonTaperAxis = Heading.getAxis(nonTaperHeading)
                nonTaperRise = cc.xrise if nonTaperAxis == "x" else cc.yrise
                xSign = Heading.getDirection3f(cc.heading).getX()
                ySign = Heading.getDirection3f(cc.heading).getY()
                if(nonTaperRise<0 or (nonTaperRise == 0 and cc.crise < 0)):
                    vcorner = LVector3f(cmi.center.getX() + cmi.radius * xSign, cmi.center.getY() + cmi.radius * ySign, cmi.center.getZ())
                    vin = vcorner - taperHeadingDir * (cmi.radius - cmi.centerComp.radius)
                    vup = LVector3f(cmi.center.getX() + cmi.radius * xSign, cmi.center.getY() + cmi.radius * ySign, cmi.center.getZ() + cmi.stepHeight)
                    
                    angle = nonTaperHeadingDir.signedAngleDeg(taperHeadingDir, LVector3f(0.0, 0.0, 1.0))
                    if(angle > 0):
                        verts1 = [vin, vcorner, vup]
                        face1 = CellFace.MakeTriangle(verts1, 1.0)
                        fList.append(face1)
                    else:
                        verts2 = [vcorner, vin, vup]
                        face2 = CellFace.MakeTriangle(verts2, 1.0)
                        fList.append(face2)
                
            elif(cc.slope == "foldednormal"):
                xSign = Heading.getDirection3f(cc.heading).getX()
                ySign = Heading.getDirection3f(cc.heading).getY()
                vin = LVector3f(cmi.center.getX() + cmi.centerComp.radius * xSign, cmi.center.getY() + cmi.centerComp.radius * ySign, cmi.center.getZ())
                maxrise = max(cc.crise, cc.xrise, cc.yrise) 
                vcout = LVector3f(cmi.center.getX() + cmi.radius * xSign, cmi.center.getY() + cmi.radius * ySign, cmi.center.getZ() + min(maxrise, 1) * cmi.stepHeight)
                vxout = LVector3f(cmi.center.getX() + cmi.radius * xSign, cmi.center.getY() + cmi.centerComp.radius * ySign, cmi.center.getZ() + min(cc.xrise, 1) * cmi.stepHeight)
                vyout = LVector3f(cmi.center.getX() + cmi.centerComp.radius * xSign, cmi.center.getY() + cmi.radius * ySign, cmi.center.getZ() + min(cc.yrise, 1) * cmi.stepHeight)
                verts = []
                if(xSign * ySign > 0):
                    verts = [vin, vxout, vcout, vyout]
                else:
                    verts = [vin, vyout, vcout, vxout]
                faces = CellFace.MakeNonPlanarSquare(verts, 1.0)
                fList.append(faces[0])
                fList.append(faces[1])
            
        return fList

###############################################################################
# Cell parameters
#
#   xnyp            yp           xpyp
#       +-----+-----------+-----+
#       | cor |           | cor |
#       | ner |    side   | ner |
#       +-----+-----------+-----+
#       |     |           |     |
#       |     |           |     |
#    xn | side|  center   | side| xp
#       |     |           |     |
#       |     |           |     |
#       +-----+-----------+-----+
#       | cor |   side    | cor |
#       | ner |           | ner |
#       +-----+-----------+-----+
#   xnyn            yn           xpyn
#
class CenterComponent:
    def __init__(self):
        self.radius = 0.0

class SideComponent:
    def __init__(self, heading):
        self.heading = heading # in "xn", "yn", "xp", "yp"
        self.rise = 0 # rise of direct neighbor
        self.slope = "" # in "flat", "block", "tapered"

class CornerComponent:
    def __init__(self, heading):
        self.heading = heading # in "xnyn", "xpyn", "xpyp", "xnyp"
        self.crise = 0 # rise of corner neighbor
        self.xrise = 0 # rise of direct neighbor in closest x direction
        self.yrise = 0 # rise of direct neighbor in closest y direction
        self.slope = "" # in "flat", "block", "taperedxn", "taperedyn", "taperedxp", "taperedyp", "foldednormal"

class NeighbCellInfo:
    def __init__(self):
        self.valid = False
        self.rise = 0

class CellMeshInfo:
    def __init__(self):
        # Invariants
        self.radius = 0.0
        self.stepHeight = 0.0

        # Center
        self.center = LVector3f(0.0, 0.0, 0.0)
        self.kHeight = 0

        # External Neighbor Info
        self.neighborInfo = {
            "xn" : NeighbCellInfo(),
            "yn" : NeighbCellInfo(),
            "xp" : NeighbCellInfo(),
            "yp" : NeighbCellInfo(),
            "xnyn" : NeighbCellInfo(),
            "xpyn" : NeighbCellInfo(),
            "xpyp" : NeighbCellInfo(),
            "xnyp" : NeighbCellInfo()
        }
    
        # Internal Mesh Components
        self.centerComp = CenterComponent()
        self.sideCompList = [
            SideComponent("xn"),
            SideComponent("yn"),
            SideComponent("yp"),
            SideComponent("xp")
        ]
        self.cornerCompList = [
            CornerComponent("xnyn"),
            CornerComponent("xpyn"),
            CornerComponent("xpyp"),
            CornerComponent("xnyp")
        ]   

###############################################################################
# Worker class meshing one cell of the terrain
class TerrainCellMesher:

    def __init__(self, terrainHeightMap, textureScheme):       
        # cell-invariant settings
        self.heightMap = terrainHeightMap
        self.textureScheme = textureScheme
        self.cmi = CellMeshInfo()
        self.cmi.radius = terrainHeightMap.cellDimension / 2.0
        self.cmi.stepHeight = terrainHeightMap.heightStep
        self.waterOffset = terrainHeightMap.waterOffset

    def __updateCenterAndHeight(self, i, j):
        # cell position settings
        self.i = i
        self.j = j
        center2i = self.heightMap.getXYLocationFromIJ(LVector2i(i,j))
        self.cmi.center = LVector3f(center2i.getX(), center2i.getY(), self.heightMap.getZHeightFromIJ(i, j))
        self.cmi.kHeight = self.heightMap.getKHeightFromIJ(i, j)
    
    def __updateTerrainCellMeshInfo(self):
        
        # neighbor cells
        for dir,nbInfo in self.cmi.neighborInfo.items():
            nbOffset = Heading.getDirection2i(dir)
            di = nbOffset.getX()
            dj = nbOffset.getY()
            if(self.heightMap.isValid(self.i + di, self.j + dj)):
                nbInfo.valid = True
                nbInfo.rise = self.heightMap.getKHeightFromIJ(self.i+di, self.j+dj) -self.cmi.kHeight
            else:
                nbInfo.valid = False
                nbInfo.rise = 0 

        # center component
        self.cmi.centerComp.radius = self.cmi.radius / 2.0

        # side components
        for sc in self.cmi.sideCompList:
            sc.rise = self.cmi.neighborInfo[sc.heading].rise
            sc.slope = "flat" if sc.rise <= 0 else "tapered"
        
        # corner components
        for cc in self.cmi.cornerCompList:
            cc.crise = self.cmi.neighborInfo[cc.heading].rise
            adjXHeading = Heading.getAdjascentXHeading(cc.heading)
            cc.xrise = self.cmi.neighborInfo[adjXHeading].rise
            adjYHeading = Heading.getAdjascentYHeading(cc.heading)
            cc.yrise = self.cmi.neighborInfo[adjYHeading].rise
            if(cc.xrise > 0 and cc.yrise <= 0):
                cc.slope = "tapered" + adjXHeading
            elif(cc.xrise <= 0 and cc.yrise > 0):
                cc.slope = "tapered" + adjYHeading
            elif(cc.xrise == 0 and cc.yrise == 0 and cc.crise > 0):
                cc.slope = "foldednormal"
            elif(cc.xrise > 0 and cc.yrise > 0):
                cc.slope = "foldednormal"
            else: #if cc.rise <= 0:
                cc.slope = "flat"

    def __meshCell(self, mesh):
        # Initialize shape
        cellShape = CellShape2()
        fList = cellShape.getFaces(self.cmi) 
        maxHeight = self.heightMap.height * self.heightMap.heightStep
        for f in fList:
            f.texMat = self.textureScheme.getMaterial(f.getVertsCentroid().getZ(), maxHeight, f.normal)
            mesh.addFace(self.textureScheme.uvMap, f)

    def __meshWater(self, mesh):
        # If water cell, add water surface face
        center3f = LVector3f(self.cmi.center.getX(), self.cmi.center.getY(), -self.waterOffset)
        cellShape = CellShape2()
        if(self.heightMap.hasWater(self.i,self.j)):
            fList = cellShape.getWaterFaces(center3f)
            for f in fList:
                f.texMat = "clearwater"
                f.color.setW(0.85)
                mesh.addFace(self.textureScheme.uvMap, f)
    
    def meshCellTerrain(self, mesh, i, j):
        self.__updateCenterAndHeight(i, j)
        self.__updateTerrainCellMeshInfo()
        self.__meshCell(mesh)

    def meshCellWater(self, mesh, i, j):   
        self.__updateCenterAndHeight(i, j)
        self.__meshWater(mesh)

###############################################################################
# Worker class generating the terrain mesh
class TerrainMesher:

    def __init__(self):
        pass

    def generateTerrain(self, size, height):
        self.heightMap = TerrainRegionMap(size, height)
        FillTerrainMapBasic(self.heightMap)
        self.textureScheme = TerrainTextureScheme()
        self.cellMesher = TerrainCellMesher(self.heightMap, self.textureScheme)
    
    def meshTerrain(self):
        terrainMesh = Mesh()
        for i in range(self.heightMap.size):
            for j in range(self.heightMap.size):
                self.cellMesher.meshCellTerrain(terrainMesh, i, j)
        return terrainMesh.makeGeom()

    def meshWater(self):
        waterMesh = Mesh()
        for i in range(self.heightMap.size):
            for j in range(self.heightMap.size):
                self.cellMesher.meshCellWater(waterMesh,i,j)
        return waterMesh.makeGeom()


