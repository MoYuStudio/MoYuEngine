from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import LVector3f, LVector3i, LVector2f, LVector2i, LVector4f

import math

#########################################################################################
# Class abstracting uv mapping in textures
# Class managing texture computation
#
#     +---------+---------+
#     |         |         |
#     |         |         |
#     |         |         |
#     +---------+---------+
#  ^  |         |         |
#  |  |         |         |
#  j  |         |         |
#     +---------+---------+
#        i -->

class TextureUVMap:
    
    def __init__(self, size):
        self.offset = 1 / size
        self.margin = self.offset * 0.1
        self.scale = self.offset - 2 * self.margin
        self.materialOffset = {}

    def addMaterial(self, name, i, j):
        self.materialOffset[name] = LVector2f(i*self.offset + self.margin, j*self.offset + self.margin)
    
    # Get UV coordinates from the right material, from xy in [0.0,1.0] range
    def getUVFromXY(self, name, x, y):
        offset = self.materialOffset[name]
        uv = LVector2f(x,y) * self.scale
        return offset + uv

###############################################################################
# Container for Mesh Data (terrain, water, etc...)
class Mesh:
    def __init__(self):
        self.format = GeomVertexFormat.getV3n3cpt2()
        self.vdata = GeomVertexData('terrain', self.format, Geom.UHDynamic)
        self.vertex = GeomVertexWriter(self.vdata, 'vertex')
        self.texcoord = GeomVertexWriter(self.vdata, 'texcoord')
        self.color = GeomVertexWriter(self.vdata, 'color')
        self.tris = GeomTriangles(Geom.UHDynamic)  
        self.normal = GeomVertexWriter(self.vdata, 'normal')
        self.numVerts = 0

    def addFace(self, textureUVMap, face):
        n = face.normal
        c = face.color
        for v in face.verts:
            self.vertex.add_data3(v.getX(), v.getY(), v.getZ())
            self.normal.addData3(n.getX(), n.getY(), n.getZ())
            self.color.addData4f(c.getX(), c.getY(), c.getZ(), c.getW())
        for tc in face.texCoords:
            schemeTC = textureUVMap.getUVFromXY(face.texMat, tc.getX(), tc.getY())
            self.texcoord.addData2f(schemeTC.getX(), schemeTC.getY())               
        mv = self.numVerts
        for t in face.triangles:
            self.tris.addVertices(mv+t.getX(), mv+t.getY(), mv+t.getZ())
        self.numVerts += len(face.verts)

    def makeGeom(self):
        geom = Geom(self.vdata)
        geom.addPrimitive(self.tris)
        return geom

###############################################################################
# Cell face class
class CellFace:
    def __init__(self):
        self.verts = []
        self.texCoords = []
        self.texMat = ""
        self.normal = []
        self.triangles = []
        self.color = LVector4f(1.0, 1.0, 1.0, 1.0)

    def updateNormalToFirstThreeVerts(self):
        v1 = self.verts[1] - self.verts[0]
        v2 = self.verts[2] - self.verts[1]
        n = v1.cross(v2)
        self.normal = n.normalized() 
    
    def fanTriangles(self):
        fan = []
        nv = len(self.verts)
        for v in range(1,nv-1):
            fan.append(LVector3i(0, v, v+1))
        self.triangles = fan

    def getVertsCentroid(self):
        sum = LVector3f(0.0, 0.0, 0.0)
        for v in self.verts:
            sum += v
        return sum * 1 / len(self.verts)
    
    def MakeSquareFace(center, normal, up, sideRadius, upRadius, refTexRadius):
        cx = center.getX()
        cy = center.getY()
        cz = center.getZ()
        sr = sideRadius
        ur = upRadius

        side = up.cross(normal)
        face = CellFace()       
        face.verts = [ 
            center - side * sideRadius - up * upRadius,
            center + side * sideRadius - up * upRadius,
            center + side * sideRadius + up * upRadius, 
            center - side * sideRadius + up * upRadius] 
        ratioSide = sideRadius / refTexRadius
        ratioUp  = upRadius / refTexRadius
        face.texCoords = [
            LVector2f(0.0, 0.0), 
            LVector2f(ratioSide, 0.0), 
            LVector2f(ratioSide, ratioUp), 
            LVector2f(0.0, ratioUp)]
        face.updateNormalToFirstThreeVerts()
        face.fanTriangles()
        return face

    def MakeNonPlanarSquare(verts, refTexRadius):
        ratio = (verts[1]-verts[0]).length() / math.sqrt(2.0) / refTexRadius

        faces = []

        face1 = CellFace() 
        face1.verts = [verts[0], verts[1], verts[2]]
        face1.texCoords = [
            LVector2f(0.0, 0.0), 
            LVector2f(ratio, 0.0), 
            LVector2f(ratio, ratio)]
        face1.updateNormalToFirstThreeVerts()
        face1.fanTriangles()
            
        face2 = CellFace() 
        face2.verts = [verts[0], verts[2], verts[3]]
        face2.texCoords = [
            LVector2f(0.0, 0.0), 
            LVector2f(ratio, ratio), 
            LVector2f(0.0, ratio)]
        face2.updateNormalToFirstThreeVerts()
        face2.fanTriangles()

        faces.append(face1)
        faces.append(face2)

        return faces

    def MakeTriangle(verts, refTexRadius):
        ratio = (verts[1]-verts[0]).length() / math.sqrt(2.0) / refTexRadius

        face = CellFace() 
        face.verts = [verts[0], verts[1], verts[2]]
        face.texCoords = [
            LVector2f(0.0, 0.0), 
            LVector2f(ratio, 0.0), 
            LVector2f(ratio, ratio)]
        face.updateNormalToFirstThreeVerts()
        face.fanTriangles()
            
        return face