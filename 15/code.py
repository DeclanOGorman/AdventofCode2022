input = [a.split(':') for a in open('./15/input.txt', 'r') ]
input = [[a[0].replace('Sensor at x=','').split(', y='), a[1].replace('closest beacon is at x=','').split(', y=')] for a in input]
input = [[tuple(map(int,a[0])), tuple(map(int,a[1]))] for a in input]

def getDist(a, b) :
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def isCovered(loc, input) :
    for s in input :
        if getDist(loc, s[0]) <= s[2] : 
            return (s[0][0]+s[2] - abs(loc[1] - s[0][1])) - loc[0]
    return -1

input = [[a[0],a[1],getDist(a[0],a[1])] for a in input]
minMaxX = (min([min(a[0][0], a[1][0]) for a in input]), max([max(a[0][0], a[1][0]) for a in input]))
minMaxY = (min([min(a[0][1], a[1][1]) for a in input]), max([max(a[0][1], a[1][1]) for a in input]))
noBeacon = 0; beacons = set([a[1] for a in input]); y = 2000000
for x in range(minMaxX[0]-100000, minMaxX[1]+100000) :
    if (x,y) in beacons : continue
    if not isCovered((x, y), input) == -1: 
        noBeacon += 1

print(f'Part A: Number of positions with no beacon {noBeacon}') # assert 26

# PART 2 needs more work, O(n^3) complexity clearly not built for brute force!! :D
b = (0,0)
for y in range(minMaxY[0], minMaxY[1]) :
    found = False
    x = minMaxX[0]
    while x <= minMaxX[1] :
        loc = (x, y)
        offset = isCovered(loc, input)
        if not offset == -1 : 
            found = True
            x = x + offset
            continue
        else :
            if found == True and isCovered((x+1,y),input) > -1 :
                b = loc
                break
        x = x+1
    if not b == (0,0): break

print(f'Part B: Decode signal at {loc} is {loc[0]*4000000 + loc[1]}') # (14,11) / 56000011



