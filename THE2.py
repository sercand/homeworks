#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs

def compare_numbers(n1, n2): # check for two numbers if they are equal
    if float("inf") == n1 and float("inf") == n2: return True
    return abs(n1-n2) <= 0.0001

def slope(v1, v2): #get the slope of a line
    if fabs(v1[0] - v2[0]) <= 0.000001: return float("inf")  #if delta x is zero, slope is infinite
    return (v1[1] - v2[1]) / (v1[0] - v2[0])  #Slope = y1-y2 / x1-x2

def length(v1, v2): #get distance between two points
    return sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2) #leght = sqrt(x1 * x2 + y1 * y2)

def turn(p, q, r): #get the direction which shows where the vector going on: left, right or none
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(hull, r):    #find next valid point on convex hull.
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != -1 \
        and not compare_numbers(slope(hull[-2],hull[-1]),slope(hull[-1],r)):
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

def convex_hull(points):#get the convex ccw polygon from given points
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
    if fabs(aSlope-bSlope) <= 0.000000001: return -1 #points are in same line
    mx = (aSlope * bSlope * (v1[1] - v3[1]) + bSlope*(v1[0] + v2[0]) -
          aSlope * (v2[0] + v3[0])) / (2 * (bSlope - aSlope))
    my = -1 * (mx - (v1[0] + v2[0]) / 2) / aSlope + (v1[1] + v2[1]) / 2
    return [mx, my, length([mx, my], v1)] #returns x of center, y of center and radius of circle

def check_line(points):#check whether 4 points in a line or not
    m = slope(points[0], points[1]) #calculate slope of first two points
    for i in range(1,len(points)-1): #check slope of other points with first point
        if not compare_numbers(m, slope(points[i], points[i+1])): return False #slope is different so this is not a line
    return True #this is a line

def check_circle(points):#check if 4 points in a circle. Points must be CCW order
    circle = calc_circle(points[0], points[1], points[2]) #calculate circle
    if circle == -1 or not compare_numbers(length(points[3], circle), circle[2]): return False #this is not circle
    return True #this is a circle, because three points means a circle and forth point is on the circle

def geo_wizard(points):
    if check_line(points): return 'line'
    ccw = convex_hull(points)
    if len(ccw) != len(points): return 'arbitraryquadrilateral'
    if check_circle(ccw): return 'circle'
    return 'triangle'
