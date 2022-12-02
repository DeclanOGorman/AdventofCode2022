with open('./2/input.txt', 'r') as f:
    input = [a.strip() for a in f]

# A/X - Rock, B/Y - Paper, C/Z - Scissors // X - Lose, Y - Draw, Z - Win
results = {'A X' : [1 + 3, 3 + 0], # [0] - Part 1 scoring, [1] - Part 2 scoring
           'A Y' : [2 + 6, 1 + 3],
           'A Z' : [3 + 0, 2 + 6],
           'B X' : [1 + 0, 1 + 0],
           'B Y' : [2 + 3, 2 + 3],
           'B Z' : [3 + 6, 3 + 6],
           'C X' : [1 + 6, 2 + 0],
           'C Y' : [2 + 0, 3 + 3],
           'C Z' : [3 + 3, 1 + 6]}

print(f'Part A: round score = {sum([results[i][0] for i in input])}') #test assert = 15 (8, 1, 6)
print(f'Part B: round score = {sum([results[i][1] for i in input])}') #test assert = 12 (4, 1, 7)