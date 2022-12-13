input = [a.strip() for a in open('./13/input.txt', 'r')]
pairs = [(int(i/3+1),input[i],input[i+1]) for i in range(0,(len(input)),3)]

def checkPairs(left, right) : # 1 correct order, 0 equal, -1 wrong
    if type(left) == int and type(right) is int:
        return 1 if left < right else -1 if right < left else 0

    if type(left) is list and type(right) is int : right = [right]
    if type(left) is int and type(right) is list : left = [left]

    for i in range(0,len(left)) :
        if i >= len(right) : return -1
        c = checkPairs(left[i],right[i])
        if c != 0 : return c
    
    return 1 if len(left) < len(right) else 0

results = [(a[0],checkPairs(eval(a[1]), eval(a[2]))) for a in pairs]
print(f'Part A: Sum of correct pairs Idx {sum([r[0] for r in results if r[1] == 1])}') # assert 13

input = [i for i in input if i != ''] + ['[[2]]','[[6]]']
output = [input[0]]
for i in input[1:] :
    for o in range(0,len(output)) :
        if checkPairs(eval(output[o]), eval(i)) == -1:
            output.insert(o, i)
            break
    if i not in output : output.append(i)

res = (output.index('[[2]]')+1) * (output.index('[[6]]')+1)
print(f'Part B: Packet decode {res}') # assert 140