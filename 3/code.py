with open('./3/input.txt', 'r') as f:
    input = [[set(a[:len(a)//2]), set(a[len(a)//2:]), set(a.strip())] for a in f]

def priority(c) : return ord(c.lower()) - 96 + (26 if c.isupper() else 0)

count = sum([priority(c) for i in input for c in i[0] if c in i[1]])
print(f'Part A: Count of misplaced items {count}') #test assert = 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); = 157.

count = sum([priority(c) for i in range(0, len(input), 3) for c in input[i][2] if c in input[i+1][2] and c in input[i+2][2]])
print(f'Part B: Count of badges {count}') #test assert = 18, 52 = 70