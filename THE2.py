#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs

def getX(vector):
    return vector[0]
def getY(vector):
    return vector[1]
def compareNumbers(n1,n2):
    return abs(n1-n2) <= 0.0001

def getSlope(v1, v2):
    return (getY(v1) - getY(v2)) / (getX(v1) - getX(v2)+0.000000001)#Slope= y1-y2 / x1-x2

def length(v1,v2):
    return sqrt((getX(v1)-getX(v2))**2 + (getY(v1)-getY(v2))**2)

def det(p, q, r):
    sum1 = q[0]*r[1] + p[0]*q[1] + r[0]*p[1]
    sum2 = q[0]*p[1] + r[0]*q[1] + p[0]*r[1]
    return sum1 - sum2

def isRightTurn((p, q, r)):
    assert p != q and q != r and p != r
    if det(p, q, r) < 0:
        return 1
    else:
        return 0

def to_right(v1, v2):
    return (v1[0]*v2[1] - v1[1]*v2[0]) < 0

def inPoly(p,poly):
    for i in range(len(poly)):
        v1 = poly[i-1]
        v2 = poly[i]
        if(to_right([v2[0]-v1[0],v2[1]-v1[1]], [p[0]-v1[0],p[1]-v1[1]])):
              return 1
    return 0

def isConcave(P):
    points = map(None, P)
    points.sort()
    upper = [points[0], points[1]]
    for p in points[2:]:
        upper.append(p)
    while len(upper) > 2 and not isRightTurn(upper[-3:]):
        del upper[-2]

    points.reverse()
    lower = [points[0], points[1]]
    for p in points[2:]:
        lower.append(p)
        while len(lower) > 2 and not isRightTurn(lower[-3:]):
            del lower[-2]

    del lower[0]
    del lower[-1]
    for x in upper:
        if x==lower[-1]:
            del lower[-1]
            break
    t = tuple(upper + lower)
    print(t)
    return len(t) != len(P)

def isPerpendicular(v1,v2,v3):#http://paulbourke.net/geometry/circlesphere/
    yDelta_a = getY(v2) - getY(v1)
    xDelta_a = getX(v2) - getX(v1)
    yDelta_b = getY(v3) - getY(v2)
    xDelta_b = getX(v3) - getX(v2)

    if ((fabs(xDelta_a) <= 0.000000001) & (fabs(yDelta_b) <= 0.000000001)):
        return False
    if (fabs(yDelta_a) <= 0.0000001):
        return True
    elif (fabs(yDelta_b) <= 0.0000001):
        return True
    elif (fabs(xDelta_a)<= 0.000000001):
        return True
    elif (fabs(xDelta_b)<= 0.000000001):
        return True
    else:
        return False

def calcCircle(v1,v2,v3):#http://paulbourke.net/geometry/circlesphere/
    yDelta_a = getY(v2) - getY(v1)
    xDelta_a = getX(v2) - getX(v1)
    yDelta_b = getY(v3) - getY(v2)
    xDelta_b = getX(v3) - getX(v2)

    if ((fabs(xDelta_a) <= 0.000000001) & (fabs(yDelta_b) <= 0.000000001)):
        mx= 0.5*(getX(v2) + getX(v3))
        my= 0.5*(getY(v1) + getY(v2))
        radius= length([mx,my],v1)
        return [mx,my,radius]

    aSlope = yDelta_a/xDelta_a
    bSlope = yDelta_b/xDelta_b
    if (fabs(aSlope-bSlope) <= 0.000000001):
        return -1
    mx= (aSlope*bSlope*(getY(v1) - getY(v3)) + bSlope*(getX(v1) + getX(v2)) -
         aSlope*(getX(v2) + getX(v3)) )/(2* (bSlope- aSlope))
    my = -1*(mx - (getX(v1) + getX(v2))/2)/aSlope + (getY(v1)+getY(v2))/2

    radius= length([mx,my],v1)
    return [mx,my,radius]

def checkLine(array, n=0):
    m = getSlope(array[0], array[1])
    for i in range(1,len(array)-1):
        if(not compareNumbers(m,getSlope(array[i], array[i+1]))):
            return False
    return True

def checkCircle(array):
    circle = -1
    if (not isPerpendicular(array[0], array[1], array[2])):
        circle = calcCircle(array[0], array[1], array[2])
    elif (not isPerpendicular(array[0], array[2], array[1])):
        circle = calcCircle(array[0], array[2], array[1])
    elif (not isPerpendicular(array[1], array[0], array[2])):
        circle = calcCircle(array[1], array[0], array[2])
    elif (not isPerpendicular(array[1], array[2], array[0])):
        circle = calcCircle(array[1], array[2], array[0])
    elif (not isPerpendicular(array[2], array[1], array[0])):
        circle = calcCircle(array[2], array[1], array[0])
    elif (not isPerpendicular(array[2], array[0], array[1])):
        circle = calcCircle(array[2], array[0], array[1])
    else:
        return False
    if circle==-1 :
        return False
    radius = length(array[3],circle)
    return compareNumbers(radius,circle[2])

def otherIndexes(a,b,array):
    x = range(0,len(array))
    x.remove(a)
    x.remove(b)
    return x

def hasTwoParallel(array):
    for i in range(len(array)):
        for j in range(i + 1 ,len(array)):
            m1 = getSlope(array[i],array[j])
            others = otherIndexes(i , j,array)
            m2 = getSlope(array[others[0]], array[others[1]])
            if(compareNumbers(m1,m2)):
                return True
    return False

def checkTriangle(array):
    return not hasTwoParallel(array)


def checkRectangle(array):
    return hasTwoParallel(array)

def geo_wizard(array):
    if checkLine(array):return 'line'
    elif checkCircle(array):return 'circle'
    elif isConcave(array):return 'arbitraryquadrilateral'
    elif checkTriangle(array):return 'triangle'
    elif checkRectangle(array):return 'rectangle'
    return 'arbitraryquadrilateral'

print geo_wizard([[1.75,-1.918698582794336],[3.1,4.948187929913334],[0.5,4.372281323269014],[5.5,-0.30277563773199456]])
print geo_wizard([[0.0,0.0],[1.0,1.0],[2.0,2.0],[3.0,3.0]])
print geo_wizard([[0, 1.5],[0.7,2.0],[2.0,1.6],[1,1]])
print geo_wizard([[0.0, 1.0], [1.0, 3.0], [2.0, 1.0], [1.0, 0.0]])
print geo_wizard([[0.0, 6.0], [3.0, 9.0], [9.0, 3.0], [6.0, 0.0]])
