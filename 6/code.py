input = [a.strip() for a in open('./6/input.txt', 'r')]

def decode (startlen) :
    buffer = []; offset = 0
    for c in input[0]:
        offset += 1
        buffer.append(c)
        if len(buffer) < startlen: continue
        if len([a for a in buffer if buffer.count(a) > 1]) == 0: break
        buffer = buffer[1:]
    return offset

print(f'Part A: Message len 4 starts at index {decode(4)}') #test assert = 7
print(f'Part B: Message len 14 starts at index {decode(14)}') #test assert = ...