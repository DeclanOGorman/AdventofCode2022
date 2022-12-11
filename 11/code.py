import math
input = [a.strip() for a in open('./11/input.txt', 'r')]

def readInstructions() : 
  for m in range(0,int((len(input) +1) / 7)):
    r = m*7
    mItems.append(list(map(int,input[r+1].replace('Starting items: ','').split(', '))))
    mOp.append(input[r+2].replace('Operation: new = ', ''))
    mTest.append(int(input[r+3].split()[-1]))
    mRes.append([int(input[r+4].split()[-1]), int(input[r+5].split()[-1])])
    mInspections.append(0)

def runMonkeys(turns, divisor, mod) :             
  for t in range(0, turns) : #turns
    for m in range(0, len(mOp)) :
      mItems[m] = [int(int(eval(mOp[m].replace('old', str(i)))) / divisor % mod) for i in mItems[m]]
      for i in mItems[m] :
        mItems[mRes[m][0] if i % mTest[m] == 0 else mRes[m][1]].append(i)
        mInspections[m] += 1
      mItems[m] = []
  return sorted(mInspections)

mItems = []; mOp = []; mTest = []; mRes = []; mInspections = []
readInstructions()
mInspections = runMonkeys(20, 3, math.inf)
monkeybusiness = mInspections[-2] * mInspections[-1]
print(f'Part A: amount of monkey business after 20 turns {monkeybusiness}') #test assert = 10605

mItems = []; mOp = []; mTest = []; mRes = []; mInspections = []
readInstructions()
mInspections = runMonkeys(10000, 1, math.prod(mTest))
monkeybusiness = mInspections[-2] * mInspections[-1]
print(f'Part B: amount of monkey business after 10000 turns {monkeybusiness}') #test assert = 10605