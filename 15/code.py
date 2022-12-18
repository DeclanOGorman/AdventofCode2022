import shapely
from shapely.geometry import LineString, Point
input = [a.split(':') for a in open('./15/input.txt', 'r') ]
input = [[a[0].replace('Sensor at x=','').split(', y='), a[1].replace('closest beacon is at x=','').split(', y=')] for a in input]
input = [[tuple(map(int,a[0])), tuple(map(int,a[1]))] for a in input]

def add(a,b) :
    return (a[0] + b[0], a[1] + b[1])

def mul(a,b) :
    return (a[0] * b, a[1] * b)

def getHash(loc) :
    return loc[0]*4000000 + loc[1]

def getDist(a, b) :
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def isCovered(loc, input) :
    for s in input :
        if getDist(loc, s[0]) <= s[2] : return True
    return False

input = [[a[0],a[1],getDist(a[0],a[1])] for a in input]
minMaxX = (min([min(a[0][0], a[1][0]) for a in input]), max([max(a[0][0], a[1][0]) for a in input]))
minMaxY = (min([min(a[0][1], a[1][1]) for a in input]), max([max(a[0][1], a[1][1]) for a in input]))
noBeacon = 0; beacons = set([a[1] for a in input]); y = 2000000
for x in range(minMaxX[0]-100000, minMaxX[1]+100000) :
    if (x,y) in beacons : continue
    if isCovered((x, y), input): 
        noBeacon += 1

print(f'Part A: Number of positions with no beacon {noBeacon}') # assert 26

# Hypothesis: the point is outside 4 sensor range edges, so intersects x4 sensor +1 vertices
vectors = [(0,1),(1,0),(0,-1),(-1,0)]; edges = []; intersect = dict()
for s, b, d in input : #Build edges +1
    p = [add(s,mul(a,(d+1))) for a in vectors]
    edges += [(p[0],p[1]),(p[1],p[2]),(p[2],p[3]),(p[3],p[0])]

for a in edges : #Find edge intersections and count
    for b in edges :
        if a == b : continue
        int_pt = LineString(a).intersection(LineString(b))

        if int_pt.is_empty == False and int_pt.type != 'LineString' :
            i = (int(int_pt.x), int(int_pt.y))
            h = getHash(i)
            if not h in intersect : intersect[h] = []
            intersect[h].append([a,b,i])

for i in intersect : 
    if len(intersect[i]) == 8 : # because we inspect each line twice 8 vs 4
        print(f'Part B: Decode signal is {i}') # (14,11) / 56000011