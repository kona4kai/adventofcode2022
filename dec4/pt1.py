input = open("dec4/input.txt", "r")
pairs = input.read().split("\n")
sum = 0

def separate(pair, sep):
    a = pair[:pair.find(sep)]
    b = pair[pair.find(sep)+1:]
    return [a, b]

def separate2(pair, sep):
    a = pair[:pair.find(sep)]
    b = pair[pair.find(sep)+1:]
    return [int(a), int(b)]

def inside(pair):
    cond1 = pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]
    cond2 = pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]
    return cond1 or cond2

x = 0
for pair in pairs:
    pairs[x] = separate(pairs[x], ",")
    for i in range(0,2):
        pairs[x][i] = separate2(pairs[x][i], "-")
    if inside(pairs[x]):
        sum += 1
    x += 1

print(sum)