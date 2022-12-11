input = [a.strip().split() for a in open('./10/input.txt', 'r')]

regX = [1]
for i in input : 
    regX.append(regX[-1])
    if i[0] != 'noop' : regX.append(regX[-1] + int(i[1]))

tot = sum([regX[r-1] * r for r in [20,60,100,140,180,220]])
print(f'Part A: Sum of registers {tot}') # asset 13140

screen = ['#' if regX[r] in [r%40-1, r%40, r%40+1] else '.' for r in range(0,len(regX))]
print('Part B: '+ ''.join(screen[:39]))
print('Part B: '+ ''.join(screen[40:79]))
print('Part B: '+ ''.join(screen[80:119]))
print('Part B: '+ ''.join(screen[120:159]))
print('Part B: '+ ''.join(screen[160:199]))
print('Part B: '+ ''.join(screen[200:239]))