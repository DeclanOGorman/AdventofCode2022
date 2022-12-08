input = [list(map(int,list(a.strip()))) for a in open('./8/input.txt', 'r')]
inputT = [list(a) for a in list(zip(*input))]

def getDist(list, val, dir) :
    if dir == 0 : list.reverse()
    for i in range(0,len(list)) :
        if list[i] >= val: return i+1
    return len(list)

visible = 0 ; maxDist = 0
for r in range(0,len(input)) :
    for c in range(0,len(input[0])) :
        v = input[r][c]; vis = False
        if len([a for a in input[r][:c] if a >= v]) == 0 : vis = True # is there a taller tree in the row
        if len([a for a in input[r][c+1:] if a >= v]) == 0 : vis = True 
        if len([a for a in inputT[c][:r] if a >= v]) == 0 : vis = True 
        if len([a for a in inputT[c][r+1:] if a >= v]) == 0 : vis = True 
        if (vis) : visible += 1

        dist = getDist(input[r][:c], v, 0) * getDist(input[r][c+1:], v, 1) * getDist(inputT[c][:r], v, 0)
        dist *= getDist(inputT[c][r+1:], v, 1)
        maxDist = max(maxDist, dist)

print(f'Part A: Number of visible trees {visible}') #test assert = 21
print(f'Part B: Best placement score {maxDist}') #test assert = 8