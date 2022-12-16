import dijkstra as di
input = [a.strip().replace('Valve ','').replace(' has flow rate=',',').replace(' tunnels lead to valves ','').replace(' tunnel leads to valve','').split(';') for a in open('./16/input.txt', 'r')]
valveRate = {a[0].split(',')[0] : int(a[0].split(',')[1]) for a in input if int(a[0].split(',')[1]) != 0}
valveMap = {a[0].split(',')[0] : a[1].split(', ') for a in input}
valves = {a for a in valveRate} | {'AA'}

g = di.Graph(); valveDist = {(a,a) : 0 for a in valves}
for e in valveMap :
    for d in valveMap[e] :
        g.add_edge(e, d, 1)
        g.add_edge(d, e, 1)

for v1 in valves :
    d = di.DijkstraSPF(g, v1)
    for v2 in valves :
        if v1 != v2 : valveDist[(v1,v2)] = d.get_distance(v2)

def findFlow(valves, time = 30, helper = False, val = 'AA') :
    f = 0
    for v in valves :
        if valveDist[(val,v)] < time :
            remain = time - valveDist[(val,v)] -1
            f = max(f, valveRate[v] * remain + findFlow(valves - {v}, remain, helper, v) + help)
    return f

valves = valves - {'AA'}
print(f'Part A: total flow after 30 mins {findFlow(valves)}') # 1651
# Part 2 to be completed... bloomin' elephants...
print(f'Part B: total flow after 26 mins with helper {findFlow(valves, 26, True)}') # test assert 1707