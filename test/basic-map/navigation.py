from panda3d.core import LVector3f, LVector3i, LVector2f, LVector2i
from itertools import cycle
import math

###############################################################################
# Heading utilities

class Heading:

    #  (7) xnyp   (6) yp   (5) xpyp
    #           +--------+
    #           |        |
    #    (0) xn |        | (4) xp
    #           |        |
    #           +--------+
    #  (1) xnyn   (2) yn   (3) xpyn

    DistDirect = 2.0
    DistCorner = 2.0 # * math.sqrt(2)

    AllSides = [ "xn", "xnyn", "yn", "xpyn", "xp", "xpyp", "yp", "xnyp" ]
    DirectSides = [ "xn", "yn", "xp", "yp" ]
    CornerSides = [ "xnyn", "xpyn", "xpyp", "xnyp" ]

    def getAxis(directHeading):
        if(directHeading=="xn" or directHeading=="xp"):
            return "x"
        elif(directHeading=="yn" or directHeading=="yp"):
            return "y"
    
    def getAdjascentHeadings(heading):
        if(heading=="xnyn"):
            return ["xn","yn"]
        elif(heading=="xpyn"):
            return ["xp","yn"]
        elif(heading=="xpyp"):
            return ["xp","yp"]
        elif(heading=="xnyp"):
            return ["xn","yp"]

    def getAdjascentXHeading(heading):
        if(heading=="xnyn"):
            return "xn"
        elif(heading=="xpyn"):
            return "xp"
        elif(heading=="xpyp"):
            return "xp"
        elif(heading=="xnyp"):
            return "xn"

    def getAdjascentYHeading(heading):
        if(heading=="xnyn"):
            return "yn"
        elif(heading=="xpyn"):
            return "yn"
        elif(heading=="xpyp"):
            return "yp"
        elif(heading=="xnyp"):
            return "yp"

    def getNextCellDist(heading):
        if(heading in Heading.DirectSides):
            return Heading.DistDirect
        else:
            return Heading.DistCorner
    
    def getRight45(heading):
        return Heading.AllSides[(Heading.AllSides.index(heading)+len(Heading.AllSides)-1)%len(Heading.AllSides)]
    def getRight90(heading):
        return Heading.AllSides[(Heading.AllSides.index(heading)+len(Heading.AllSides)-2)%len(Heading.AllSides)]
    def getLeft45(heading):
        return Heading.AllSides[(Heading.AllSides.index(heading)+1)%len(Heading.AllSides)]
    def getLeft90(heading):
        return Heading.AllSides[(Heading.AllSides.index(heading)+2)%len(Heading.AllSides)]
    def getOpposite(heading):
        return Heading.AllSides[round(Heading.AllSides.index(heading)+len(Heading.AllSides)/2)%len(Heading.AllSides)]
    
    def getDirection2i(heading):
        if(heading=="xn"):
            return LVector2i(-1, 0)
        elif(heading=="xnyn"):
            return LVector2i(-1, -1)
        elif(heading=="yn"):
            return LVector2i(0, -1)
        elif(heading=="xpyn"):
            return LVector2i(1, -1)
        elif(heading=="xp"):
            return LVector2i(1, 0)
        elif(heading=="xpyp"):
            return LVector2i(1, 1)
        elif(heading=="yp"):
            return LVector2i(0, 1)
        elif(heading=="xnyp"):
            return LVector2i(-1, 1)

    def getDirection3f(heading):
        if(heading=="xn"):
            return LVector3f(-1.0, 0.0, 0.0)
        elif(heading=="xnyn"):
            return LVector3f(-1.0, -1.0, 0.0)
        elif(heading=="yn"):
            return LVector3f(0.0, -1.0, 0.0)
        elif(heading=="xpyn"):
            return LVector3f(1.0,-1.0, 0.0)
        elif(heading=="xp" or heading=="x"):
            return LVector3f(1.0, 0.0, 0.0)
        elif(heading=="xpyp"):
            return LVector3f(1.0, 1.0, 0.0)
        elif(heading=="yp" or heading=="y"):
            return LVector3f(0.0, 1.0, 0.0)
        elif(heading=="xnyp"):
            return LVector3f(-1.0, 1.0, 0.0)