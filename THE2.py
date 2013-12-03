#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs

def getX(vector):
    return vector[0]

def getY(vector):
    return vector[1]

def compare_numbers(n1, n2):
    if float("inf") == n1 and float("inf") == n2:
        return True
    return abs(n1-n2) <= 0.0001

def slope(v1, v2):
    delta_x = getX(v1) - getX(v2)
    if fabs(delta_x) <= 0.0001:
        return float("inf")
    return (getY(v1) - getY(v2)) / (delta_x)  #Slope= y1-y2 / x1-x2

def length(v1, v2):
    return sqrt((getX(v1)-getX(v2))**2 + (getY(v1)-getY(v2))**2)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != -1 \
        and not compare_numbers(slope(hull[-2],hull[-1]),slope(hull[-1],r)):
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):
    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

def calc_circle(v1,v2,v3):
    yDelta_a = getY(v2) - getY(v1)
    xDelta_a = getX(v2) - getX(v1)
    yDelta_b = getY(v3) - getY(v2)
    xDelta_b = getX(v3) - getX(v2)
    if fabs(xDelta_a) <= 0.000000001 and fabs(yDelta_b) <= 0.000000001:
        mx = 0.5*(getX(v2) + getX(v3))
        my = 0.5*(getY(v1) + getY(v2))
        radius= length([mx,my],v1)
        return [mx,my,radius]
    aSlope = yDelta_a/(xDelta_a + 0.000000001)
    bSlope = yDelta_b/(xDelta_b + 0.000000001)
    if fabs(aSlope-bSlope) <= 0.000000001:
        return -1
    mx = (aSlope * bSlope * (getY(v1) - getY(v3)) + bSlope*(getX(v1) + getX(v2)) -
          aSlope * (getX(v2) + getX(v3))) / (2 * (bSlope - aSlope))
    my = -1 * (mx - (getX(v1) + getX(v2)) / 2) / aSlope + (getY(v1) + getY(v2)) / 2
    radius = length([mx, my], v1)
    return [mx, my, radius]

def check_line(array):
    m = slope(array[0], array[1])
    for i in range(1,len(array)-1):
        if not compare_numbers(m, slope(array[i], array[i+1])):
            return False
    return True

def check_circle(array):
    circle = calc_circle(array[0], array[1], array[2])
    if circle==-1: return False
    for i in range(3,len(array)):
        if not compare_numbers(length(array[i],circle), circle[2]):
            return False
    return True

def geo_wizard(array):
    if check_line(array): return 'line'
    ccw = convex_hull(array)
    if len(ccw) != len(array): return 'arbitraryquadrilateral'
    if check_circle(ccw): return 'circle'
    else: return 'triangle'

print geo_wizard([[1.75,-1.918698582794336],[3.1,4.948187929913334], [0.5,4.372281323269014],[5.5,-0.30277563773199456]])
print geo_wizard([[0,0],[0,2], [2,2],[2,0]])
print geo_wizard([[0,0],[2,2], [2,0],[1,0]])
print geo_wizard([[0,0],[2,2], [2,0],[1,0.5]])
print geo_wizard([[1.0,0.0], [1.0,5.0], [1.0,3.0], [1.0,2.0]])
print geo_wizard([[1.0,1.0],[2.0,2.0], [3.0,3.0],[4.0,4.0]])
print geo_wizard([[0.0, 0.0], [0.0, 6.0],[+1.5, 0.40192378864], [3.0, 3.0]])
