# more time wasted than i'd care to admit trying to build my own Dijkstra algo, one day i'll learn!!
import dijkstra as di
input = [list(a.strip()) for a in open('./12/input.txt', 'r')]

def findLoc(loc) : 
    sY = [i for i in range(0,len(input)) if loc in input[i]][0]
    return (input[sY].index(loc), sY)

def canStep(curr, step) :
    return ord(step.replace('E','z')) - ord(curr.replace('S','a')) <= 1

def buildGraph() :          
    g = di.Graph()
    for x in range(0,len(input[0])) :
        for y in range(0, len(input)) :
            for o in (1,0),(0,1),(0,-1),(-1,0) :
                x2 = x + o[1]; y2 = y + o[0]
                if x2 < 0 or y2 < 0 or x2 >= len(input[0]) or y2 >= len(input) or \
                    not canStep(input[y][x], input[y2][x2]) : continue
                else : g.add_edge(str((x,y)), str((x2,y2)), 1)
    return g

start = findLoc('S'); end = findLoc('E')
g = buildGraph()
d = di.DijkstraSPF(g, str(start))
print(f'Part A: Steps to complete route {d.get_distance(str(end))}') # assert 31

minDist = 999999
for x in range(0,len(input[0])) :
    for y in range(0, len(input)) :
        if input[y][x] == 'a' :
            d = di.DijkstraSPF(g, str((x,y)))
            minDist = min(minDist, d.get_distance(str(end)))

print(f'Part B: Steps to complete route from nearest a {minDist}') # assert 