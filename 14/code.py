input = [[tuple(map(int,b.split(','))) for b in a.strip().split(' -> ')] for a in open('./14/input.txt', 'r') ]
sandStart = (500,0); sandFall = [(0,1), (-1,1), (1,1)]

def findWalls(input) :
    walls = set()
    for i in input :
        for j in range(0,len(i)-1) :
            v1 = i[j]; v2 = i[j+1]
            walls = walls.union([(x, v1[1]) for x in range (min(v1[0],v2[0]), max(v1[0],v2[0])+1)])
            walls = walls.union([(v1[0], y) for y in range (min(v1[1],v2[1]), max(v1[1],v2[1])+1)])
    return walls

def dropSand(walls) :
    sand = set(); maxX = max([a[0] for a in walls]); maxY = max([a[1] for a in walls])
    while True : # drop sand
        s = sandStart
        while True : # iterate falling
            for f in sandFall : #test each pathway in order
                s2 = (s[0] + f[0], s[1] + f[1]);  end = True
                if not s2 in sand and not s2 in walls: #if not obstructed continue to fall
                    s = s2; end = False
                    break
            if end: sand.add(s) # if at resting spot add to set
            if s[0] > maxX or s[1] > maxY or end or s == (500,0) :
                break
        if s[0] > maxX or s[1] > maxY or s == (500,0) :
            break
    return sand

walls = findWalls(input)
print(f'Part A: Amount of sand dropped {len(dropSand(walls))}') # assert 24

maxY = max([a[1] for a in walls])
input.append([(500-maxY-30, maxY+2),(500+maxY+30, maxY+2)]) # add floor
print(f'Part B: Amount of sand dropped with floor {len(dropSand(findWalls(input)))}') # assert 24