#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs

def compare_numbers(n1, n2): # check for two numbers if they are equal
    if float("inf") == n1 and float("inf") == n2: return True
    return abs(n1-n2) <= 0.0001

def slope(v1, v2): #get the slope of a line
    if fabs(v1[0] - v2[0]) <= 0.000001:  #if delta x is zero, slope is infinite
        return float("inf")
    return (v1[1] - v2[1]) / (v1[0] - v2[0])  #Slope = y1-y2 / x1-x2

def length(v1, v2): #get distance between two points
    return sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2) #leght = sqrt(x1 * x2 + y1 * y2)

def turn(p, q, r):#get the direction which shows where the vector going on: left, right or none
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != -1 \
        and not compare_numbers(slope(hull[-2],hull[-1]),slope(hull[-1],r)):
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):#get the convex ccw polygon form given points
    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

def calc_circle(v1,v2,v3):#calculate a circle from 3 points
    yDelta_a ,xDelta_a= v2[1] - v1[1], v2[0] - v1[0]
    yDelta_b ,xDelta_b  = v3[1] - v2[1], v3[0] - v2[0]
    if fabs(xDelta_a) <= 0.000000001 and fabs(yDelta_b) <= 0.000000001:
        mx = 0.5*(v2[0] + v3[0])
        my = 0.5*(v1[1] + v2[1])
        return [mx,my, length([mx,my],v1)] #returns x of center, y of center and radius of circle
    aSlope = yDelta_a/(xDelta_a + 0.000000001)
    bSlope = yDelta_b/(xDelta_b + 0.000000001)
    if fabs(aSlope-bSlope) <= 0.000000001: return -1
    mx = (aSlope * bSlope * (v1[1] - v3[1]) + bSlope*(v1[0] + v2[0]) -
          aSlope * (v2[0] + v3[0])) / (2 * (bSlope - aSlope))
    my = -1 * (mx - (v1[0] + v2[0]) / 2) / aSlope + (v1[1] + v2[1]) / 2
    return [mx, my, length([mx, my], v1)] #returns x of center, y of center and radius of circle

def check_line(array):
    m = slope(array[0], array[1])
    for i in range(1,len(array)-1):
        if not compare_numbers(m, slope(array[i], array[i+1])): return False
    return True

def check_circle(array):
    circle = calc_circle(array[0], array[1], array[2])
    if circle == -1 or not compare_numbers(length(array[3], circle), circle[2]): return False
    return True

def geo_wizard(array):
    if check_line(array): return 'line'
    ccw = convex_hull(array)
    if len(ccw) != len(array): return 'arbitraryquadrilateral'
    if check_circle(ccw): return 'circle'
    return 'triangle'

print geo_wizard([[0,0],[0,1],[0,2],[0,3]])
print geo_wizard([[1.75,-1.918698582794336],[3.1,4.948187929913334], [0.5,4.372281323269014],[5.5,-0.30277563773199456]])
print geo_wizard([[0,0],[2,2], [2,0],[1,0.5]])
print geo_wizard([[1.0,0.0], [1.0,5.0], [1.0,3.0], [1.0,2.0]])
print geo_wizard([[1.0,1.0],[2.0,2.0], [3.0,3.0],[4.0,4.0]])
print geo_wizard([[0.0, 0.0], [0.0, 6.0],[+1.5, 0.40192378864], [3.0, 3.0]])
print geo_wizard([[0,0],[0,2], [2,2],[2,0]])
print geo_wizard([[0,0],[2,2], [2,0],[1,0]])
