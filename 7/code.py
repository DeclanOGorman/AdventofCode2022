input = [a.strip() for a in open('./7/input.txt', 'r')]

fs = {}; cwd = {}; crumbs = []
for a in input :
    if a.startswith('$') :
        if a == '$ cd /' :
            cwd = fs
        elif a == '$ cd ..' :
            cwd = crumbs.pop()
        elif a == '$ ls' :
            continue
        else :
            crumbs.append(cwd)
            cwd = cwd[a.replace('$ cd ','')]
    else :
        l = a.split()
        if l[0] == 'dir' :
            cwd[l[1]] = {}
        else :
            cwd[l[1]] = int(l[0]) 

def size(fs, sizeList) :
    s = [0,0,70000000]
    for a in fs :
        if type(fs[a]) is dict:
            dirsize = size(fs[a], sizeList)
            s[0] += dirsize[0]; s[1] += dirsize[1]; s[2] = dirsize[2]
        else :
            s[0] += fs[a]
    sizeList.append(s[0])
    return [s[0], s[1] if s[0] >= 100000 else s[1] + s[0], 0]

dirSizes = []
s10 = size(fs, dirSizes)
print(f'Part A: Size of dirs <10k {s10[1]}') #test assert = 95437

spaceNeeded = 30000000 - (70000000 - s10[0])
s10 = size(fs, dirSizes)
dir = min([d for d in dirSizes if d >= spaceNeeded])
print(f'Part B: Space needed {spaceNeeded}, dir to delete {dir}') #test assert = ...