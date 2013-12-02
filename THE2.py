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

TURN_RIGHT, TURN_NONE = ( -1, 0)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _dist(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    return dx * dx + dy * dy

def _next_hull_pt(points, p):
    q = p
    for r in points:
        t = turn(p, q, r)
        if t == TURN_RIGHT or t == TURN_NONE and _dist(p, r) > _dist(p, q):
            q = r
    return q

def convex_hull(points):#http://tomswitzer.net/2009/12/jarvis-march/
    hull = [min(points)]
    for p in hull:
        q = _next_hull_pt(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull

def isConcave(P):
    t = convex_hull(P)
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

def otherIndexes(a,b,array):
    x = range(0,len(array))
    x.remove(a)
    x.remove(b)
    return x

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

def geo_wizard(array):
    if checkLine(array):return 'line'
    elif checkCircle(array):return 'circle'
    elif isConcave(array):return 'arbitraryquadrilateral'
    else: return 'triangle'