#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs

def getX(vector):
    return vector[0]

def getY(vector):
    return vector[1]

def compareNumbers(n1, n2):
    return abs(n1-n2) <= 0.0001

def getSlope(v1, v2):
    return (getY(v1) - getY(v2)) / (getX(v1) - getX(v2)+0.000000001)  #Slope= y1-y2 / x1-x2

def length(v1,v2):
    return sqrt((getX(v1)-getX(v2))**2 + (getY(v1)-getY(v2))**2)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != -1 \
        and not compareNumbers(getSlope(hull[-2],hull[-1]),getSlope(hull[-1],r)):
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

def is_convex(P):
    t = convex_hull(P)
    return len(t) == len(P)

def is_perpendicular(v1,v2,v3):#http://paulbourke.net/geometry/circlesphere/
    yDelta_a = getY(v2) - getY(v1)
    xDelta_a = getX(v2) - getX(v1)
    yDelta_b = getY(v3) - getY(v2)
    xDelta_b = getX(v3) - getX(v2)
    if fabs(xDelta_a) <= 0.000000001 and fabs(yDelta_b) <= 0.000000001:
        return False
    if abs(yDelta_a)<=0.0000001 or abs(yDelta_b)<=0.0000001 or abs(xDelta_a)<=0.000000001 or abs(xDelta_b)<=0.000000001:
        return True
    else:
        return False

def calc_circle(v1,v2,v3):#http://paulbourke.net/geometry/circlesphere/
    yDelta_a = getY(v2) - getY(v1)
    xDelta_a = getX(v2) - getX(v1)
    yDelta_b = getY(v3) - getY(v2)
    xDelta_b = getX(v3) - getX(v2)
    if fabs(xDelta_a) <= 0.000000001 and fabs(yDelta_b) <= 0.000000001:
        mx = 0.5*(getX(v2) + getX(v3))
        my = 0.5*(getY(v1) + getY(v2))
        radius= length([mx,my],v1)
        return [mx,my,radius]
    aSlope = yDelta_a/xDelta_a
    bSlope = yDelta_b/xDelta_b
    if fabs(aSlope-bSlope) <= 0.000000001:
        return -1
    mx = (aSlope*bSlope*(getY(v1) - getY(v3)) + bSlope*(getX(v1) + getX(v2)) -
         aSlope*(getX(v2) + getX(v3)) ) / (2* (bSlope - aSlope))
    my = -1*(mx - (getX(v1) + getX(v2)) / 2) / aSlope + (getY(v1) + getY(v2)) / 2
    radius = length([mx,my],v1)
    return [mx,my,radius]

def check_line(array):
    m = getSlope(array[0], array[1])
    for i in range(1,len(array)-1):
        if not compareNumbers(m, getSlope(array[i], array[i+1])):
            return False
    return True

def check_circle(array):
    circle = -1
    if not is_perpendicular(array[0], array[1], array[2]):
        circle = calc_circle(array[0], array[1], array[2])
    elif not is_perpendicular(array[0], array[2], array[1]):
        circle = calc_circle(array[0], array[2], array[1])
    elif not is_perpendicular(array[1], array[0], array[2]):
        circle = calc_circle(array[1], array[0], array[2])
    elif not is_perpendicular(array[1], array[2], array[0]):
        circle = calc_circle(array[1], array[2], array[0])
    elif not is_perpendicular(array[2], array[1], array[0]):
        circle = calc_circle(array[2], array[1], array[0])
    elif not is_perpendicular(array[2], array[0], array[1]):
        circle = calc_circle(array[2], array[0], array[1])
    else:
        return False
    if circle == -1 :
        return False
    for i in range(3,len(array)):
        radius = length(array[i],circle)
        if not compareNumbers(radius, circle[2]):
            return False
    return True

def geo_wizard(array):
    if check_line(array): return 'line'
    elif check_circle(array): return 'circle'
    elif is_convex(array): return 'triangle'
    else: return 'arbitraryquadrilateral'
