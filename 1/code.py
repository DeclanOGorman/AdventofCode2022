with open('./1/input.txt', 'r') as f:
    input = [a.strip() for a in f]

cals = [[]]
for c in input:
    if c == '': cals.append([])
    else: cals[len(cals)-1].append(int(c))

sums = sorted([sum(a) for a in cals],reverse=True)
print(f'Part A: max cals = {sums[0]}') #test assert = 24000
print(f'Part B: top 3 max cals = {sums[0] + sums[1] + sums[2]}') #test assert = 45000