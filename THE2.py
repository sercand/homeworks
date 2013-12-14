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

def check_point(h, r): #find next valid point on convex hull.
    while len(h)>1 and cmp((h[-1][0]-h[-2][0])*(r[1]-h[-2][1])-(r[0]-h[-2][0])*(h[-1][1]-h[-2][1]), 0) != -1 \
        and not compare(slope(h[-2],h[-1]),slope(h[-1],r)): h.pop()
    if not len(h) or h[-1] != r: h.append(r)
    return h

def calc_circle(v1,v2,v3):#calculate a circle from 3 points
    cx, cy, m1, m2 = inf, inf, slope(v2, v1), slope(v3, v2)
    if compare(m1,m2):return -1
    if compare(m1, 0.0) : cx = 0.5*(v1[0] + v2[0])
    elif compare(m2, 0) : cx = 0.5*(v3[0] + v2[0])
    if compare(m1, inf) : cy = 0.5*(v1[1] + v2[1])
    elif compare(m2,inf): cy = 0.5*(v3[1] + v2[1])
    if compare(cx, inf) and compare(cy, inf):
        cx = (m1 * m2 * (v1[1] - v3[1]) + m2*(v1[0] + v2[0]) - m1 * (v2[0] + v3[0])) / (2 * (m2 - m1))
        cy = -1 * (cx - (v1[0] + v2[0]) / 2) / m1 + (v1[1] + v2[1]) / 2
    elif not compare(cx, inf) and not compare(cy, inf): return [cx, cy, length([cx, cy], v1)]
    elif compare(m2, inf): cx = (v2[0]+v1[0])/2 + (cy -(v2[1]+v1[1])/2) / (-1/m1)
    elif compare(m1, inf): cx = (v3[0]+v2[0])/2 + (cy -(v3[1]+v2[1])/2) / (-1/m2)
    elif compare(m2, 0.0): cy = (v2[1]+v1[1])/2 + (cx -(v2[0]+v1[0])/2) * (-1/m1)
    elif compare(m1, 0.0): cy = (v3[1]+v2[1])/2 + (cx -(v3[0]+v2[0])/2) * (-1/m2)
    return [cx, cy, length([cx, cy], v1)]

def geo_wizard(ps):
    ccw, m1, m2, l, u = sorted(ps), slope(ps[0], ps[1]), slope(ps[0], ps[2]), [], []
    if compare(m1, m2) and compare(m1, slope(ps[0], ps[3])): return 'line'
    for r in ccw: l = check_point(l,r)
    for r in ccw[::-1]: u = check_point(u,r)
    ccw = l.extend(u[1:len(u)-1]) or l
    if len(ccw) != len(ps): return 'arbitraryquadrilateral'
    circle = calc_circle(ccw[0],ccw[1],ccw[2])
    if circle == -1 or not compare(circle[2], length(ccw[3], circle)): return 'triangle'
    return 'circle'