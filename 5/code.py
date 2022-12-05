input = [a for a in open('./5/input.txt', 'r')]
numstacks = 9; stacks = {i+1 : [] for i in range(0,numstacks)}

def buildStack(numstacks, stacks) :
    for r in input: # build input stacks
        if not str(r).startswith('[') or str(r).startswith('  ') : break
        for i in range(0,numstacks):
            if r[1 + (i * 4)] != ' ' : stacks[i+1].insert(0, r[1 + (i * 4)])

buildStack(numstacks, stacks)
for r in input : 
    if r.startswith('move') : 
        ins = r.replace('move ', '').replace(' from ',',').replace(' to ',',').split(',')
        ins = list(map(int, ins))
        for i in range(0,ins[0]) :
            stacks[ins[2]].append(stacks[ins[1]].pop())

code = ''.join([stacks[s][-1] for s in stacks])
print(f'Part A: Rearranged crates top items {code}') #test assert = CMZ

stacks = {i+1 : [] for i in range(0,numstacks)}
buildStack(numstacks, stacks)
for r in input : 
    if r.startswith('move') : 
        ins = r.replace('move ', '').replace(' from ',',').replace(' to ',',').split(',')
        ins = list(map(int, ins))
        
        temp = [] # just updated from Part A to keep order
        for i in range(0,ins[0]) :
            c = stacks[ins[1]].pop()
            temp.append(c)
            
        for i in range(0,ins[0]) :
            c = temp.pop()
            stacks[ins[2]].append(c)

code = ''.join([stacks[s][-1] for s in stacks])
print(f'Part B: Rearranged crates top items {code}') #test assert = ...