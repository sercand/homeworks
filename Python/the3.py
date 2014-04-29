#Created by Sercan Degirmenci on 28.12.2013
from math import sqrt
inf = float("inf")

def length(v1, v2):
    da, db = (v1[0] - v2[0]), (v1[1] - v2[1])
    return sqrt(da * da + db * db)

def do_it(points, index):
    if len(points) == 1 : return 0 , points
    p0, j, shortest = points.pop(index), 0, inf
    for i in xrange(0, len(points)):
        d = length(p0, points[i])
        if d < shortest: j, shortest = i, d
    new = do_it(points, j)
    return shortest + new[0], [p0] + new[1]

def order(points):
    shortest, points = (inf, []), sorted(points)
    for i in xrange(0, len(points)):
        temp = do_it(points[:], i)
        if temp[0] < shortest[0]: shortest = temp
    return shortest[1]
