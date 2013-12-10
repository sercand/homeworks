#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs
inf = float("inf") #For performance, initialize inf number only once
def compare(n1, n2): # check for two numbers if they are equal
    return (inf == n1 and inf == n2) or (fabs(n1-n2) <= 0.0001)

def slope(v1, v2): #get the slope of a line
    if fabs(v1[0] - v2[0]) <= 0.000001: return inf  #if delta x is zero, slope is infinite
    return (v1[1] - v2[1]) / (v1[0] - v2[0])  #Slope = y1-y2 / x1-x2

def length(v1, v2): #get distance between two points
    da, db = (v1[0] - v2[0]), (v1[1] - v2[1])
    return sqrt(da * da + db * db)

def turn(p, q, r): #get the direction which shows where the vector going on: left, right or none
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def keep_left(h, r): #find next valid point on convex hull.
    while len(h) > 1 and turn(h[-2], h[-1], r) != -1 and not compare(slope(h[-2],h[-1]),slope(h[-1],r)): h.pop()
    if not len(h) or h[-1] != r: h.append(r)
    return h

def geo_wizard(points):
    m1, m2 = slope(points[0], points[1]), slope(points[0], points[2])
    if compare(m1, m2) and compare(m1, slope(points[0], points[3])):  return 'line'
    points = sorted(points)
    l = reduce(keep_left, points, [])
    u = reduce(keep_left, points[::-1], [])
    ccw = l.extend(u[i] for i in xrange(1, len(u) - 1)) or l
    if len(ccw) != len(points): return 'arbitraryquadrilateral'
    aSlope = (ccw[1][1] - ccw[0][1])/(ccw[1][0] - ccw[0][0] + 0.000000001)
    bSlope = (ccw[2][1] - ccw[1][1])/(ccw[2][0] - ccw[1][0] + 0.000000001)
    if fabs(aSlope-bSlope) <= 0.000000001: return 'triangle'
    mx = (aSlope * bSlope * (ccw[0][1] - ccw[2][1]) + bSlope*(ccw[0][0] + ccw[1][0]) -
          aSlope * (ccw[1][0] + ccw[2][0])) / (2 * (bSlope - aSlope))
    my = -1 * (mx - (ccw[0][0] + ccw[1][0]) / 2) / aSlope + (ccw[0][1] + ccw[1][1]) / 2
    if compare(length([mx, my], ccw[0]), length(ccw[3], [mx, my])): return 'circle'
    return 'triangle'