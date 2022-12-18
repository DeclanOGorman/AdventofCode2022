input = [list(a) for a in open('./17/input.txt', 'r')][0]

shapes = []
shapes.append([{(0,0),(1,0),(2,0),(3,0)},4]) # -
shapes.append([{(1,0),(0,1),(1,1),(2,1),(1,2)},3]) # +
shapes.append([{(2,2),(2,1),(0,0),(1,0),(2,0)},3]) # backwards L
shapes.append([{(0,0),(0,1),(0,2),(0,3)},1]) # |
shapes.append([{(0,0),(1,0),(0,1),(1,1)},2]) # square
gas = {'<' : (-1,0), '>' : (1,0)}
width = 7; dropOffset = 4; prior = dict()

def maxHeight(rocks) : return max([y for x,y in rocks])
def tAdd(a, b) : return tuple(map(sum, zip(a, b)))
def sAdd(a, s) : return {tAdd(a,p) for p in s}

def runGame(shapeLimit, exitOnRec = False) :
    turn = 0; shape = 0; recurring = 0
    rocks = (set([(x,0) for x in range(0,width)])) # Add Floor
    while shape < shapeLimit :
        # for Part 2, check if we've seen this setup before
        # Took a while after failing with turn/shape product combos!
        k = (shape % len(shapes), turn % len(input))
        top = maxHeight(rocks)
        if k in prior :
            step, topP = prior[k]
            if shape-step != 0 : 
                div, mod = divmod(1000000000000-shape, shape-step)
                if mod == 0 : 
                    recurring = int(top + (top-topP) * div)
                    if exitOnRec : break
        else : 
            prior[k] = shape, top

        s = shapes[shape % len(shapes)]
        shape += 1
        pos = (2, maxHeight(rocks) + dropOffset) # start at max + 4 & 3 from edge
        while True: # iterate moves until landed
            pos2 = tAdd(pos, gas[input[turn % len(input)]]) # gas push if not blocked
            turn += 1
            if pos2[0] < 0 or pos2[0] + s[1]-1 >= width or \
                not rocks.isdisjoint(sAdd(pos2, s[0])) :
                pos2 = pos # if blocked dont move
            
            pos = tAdd(pos2, (0,-1)) # drop if not blocked
            if not sAdd(pos, s[0]).isdisjoint(rocks) :
                rocks.update(sAdd(pos2, s[0])) # if blocked convert to rock
                break
    return rocks, recurring

r, rec = runGame(2022)
print(f'Part A: Stack is {maxHeight(r)} tall after 2022 turns') # assert 3068

r, rec = runGame(10000, True)
print(f'Part B: Stack is {rec} tall after 1000000000000 turns') # assert 1514285714288