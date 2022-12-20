input = set([tuple(map(int,a.strip().split(','))) for a in open('./18/input.txt', 'r')])
adjSides  = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def tAdd(a,b) : return (a[0]+b[0], a[1]+b[1], a[2]+b[2]) 
def tBetween(a,mm) : return mm[0][0] <= a[0] <= mm[0][1] and mm[1][0] <= a[1] <= mm[1][1] and mm[2][0] <= a[2] <= mm[2][1]

s = sum([1 for i in input for x in adjSides if tAdd(i,x) not in input])
print(f'Part A: {s} sides showing')   

minMax = [(0,20),(0,20),(0,20)]; visited = set()
flood = {(minMax[0][0],minMax[1][0],minMax[2][0])}
total = set([(x,y,z) for x in range(minMax[0][0],minMax[0][1]) for y in range(minMax[1][0],minMax[1][1]) for z in range(minMax[2][0],minMax[2][1])])
while len(flood) > 0 :
    f = flood.pop()
    visited.add(f)
    if not f in input :
        newPoints = [tAdd(f,s) for s in adjSides]
        flood.update(set([s for s in newPoints if tBetween(s,minMax) and not s in visited]))

s2 = sum([1 for i in total - visited - input for x in adjSides if tAdd(i,x) in input])
print(f'Part B: {s - s2} sides showing minus airpockets')   