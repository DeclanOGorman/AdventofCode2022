input = [a.strip().split(': ') for a in open('./19/test.txt', 'r')]
blueRules = [[int(a[0].split(' ')[1]), dict(), a[1].split('. ')] for a in input]
print(blueRules)
for r in blueRules: 
    for rob in r[2] :
        r[1][rob.split(' ')[1]] = [[int(a.split(' ')[0]),a.split(' ')[1].replace('.','')] for a in rob.split('costs ')[1].split(' and ')]
print(' ')
print(blueRules)

def runMining(mins) :
    for i in range(1,mins + 1) :


print(f'Part A: ... {...}')