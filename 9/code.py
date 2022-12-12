import numpy as np # pip install numpy
input = [a.strip().split() for a in open('./9/input.txt', 'r')]
moves = {'U' : (0,1), 'D' : (0,-1), 'L' : (-1,0), 'R' : (1,0)}

def runRope(knots) :
    positions = set(); rope = [(0,0) for i in range(0,knots)]
    for i in input :
        for m in range(0,int(i[1])) :
            rope[0] = tuple(np.add(rope[0], moves[i[0]]))
            for r in range(0,len(rope) -1) :
                diff = np.subtract(rope[r], rope[r+1])
                move = (0,0)
                if abs(diff[0]) >1 or abs(diff[1]) > 1 :
                    move = (int(diff[0]/2) if abs(diff[0]) == 2 else diff[0], int(diff[1]/2) if abs(diff[1]) == 2 else diff[1] )
                rope[r+1] = tuple(np.add(rope[r+1], move))
            positions.add(rope[-1])
    return positions

print(f'Part A: positions visited with rope len 2 - {len(runRope(2))}') # assert 13
print(f'Part B: positions visited with rope len 10 - {len(runRope(10))}') # assert ...