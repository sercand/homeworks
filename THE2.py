#Created by Sercan Degirmenci on 29.11.2013
from math import sqrt, fabs
inf = float("inf")
def compare(n1, n2):
    return (inf == n1 and inf == n2) or (fabs(n1-n2) <= 0.0001)

def slope(v1, v2):
    if fabs(v1[0] - v2[0]) <= 0.0000001: return inf
    return (v1[1] - v2[1]) / (v1[0] - v2[0])

def length(v1, v2):
    da, db = (v1[0] - v2[0]), (v1[1] - v2[1])
    return sqrt(da * da + db * db)

def check_point(h, r):
    while len(h)>1 and cmp((h[-1][0]-h[-2][0])*(r[1]-h[-2][1])-(r[0]-h[-2][0])*(h[-1][1]-h[-2][1]), 0) != -1 \
        and not compare(slope(h[-2],h[-1]),slope(h[-1],r)): h.pop()
    if not len(h) or h[-1] != r: h.append(r)
    return h

def geo_wizard(ps):
    ccw, m1, m2, l, u = sorted(ps), slope(ps[0], ps[1]), slope(ps[0], ps[2]), [], []
    if compare(m1, m2) and compare(m1, slope(ps[0], ps[3])): return 'line'
    for r in ccw: l = check_point(l,r)
    for r in ccw[::-1]: u = check_point(u,r)
    ccw = l.extend(u[1:len(u)-1]) or l
    if len(ccw) != len(ps): return 'arbitraryquadrilateral'
    ma = (ccw[1][1] - ccw[0][1]+ 0.000000001)/(ccw[1][0] - ccw[0][0] + 0.000000001)
    mb = (ccw[2][1] - ccw[1][1]+ 0.000000001)/(ccw[2][0] - ccw[1][0] + 0.000000001)
    if fabs(ma-mb) <= 0.000000001: return 'triangle'
    cx = (ma*mb*(ccw[0][1]-ccw[2][1])+mb*(ccw[0][0]+ccw[1][0]) - ma*(ccw[1][0]+ccw[2][0]))/(2*(mb-ma))
    cy = -1 * (cx - (ccw[0][0] + ccw[1][0]) / 2) / ma + (ccw[0][1] + ccw[1][1]) / 2
    if compare(length([cx, cy], ccw[0]), length(ccw[3], [cx, cy])): return 'circle'
    return 'triangle'