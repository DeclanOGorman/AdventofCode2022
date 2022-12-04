input = [list(map(int,a.strip().replace('-',',').split(','))) for a in open('./4/input.txt', 'r')]
input = [[set(range(a[0],a[1]+1)), set(range(a[2],a[3]+1))] for a in input]

overlaps = [i for i in input if i[0].issubset(i[1]) or i[1].issubset(i[0])]
print(f'Part A: Fully overlapping assignments {len(overlaps)}') #test assert = 2 

overlaps = [i for i in input if not i[0].isdisjoint(i[1])]
print(f'Part B: Partially overlapping assignments {len(overlaps)}') #test assert = 4