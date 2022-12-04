# Messy, but coding fast
input = open("dec3/input.txt", "r")

def shared(a, b):
    for char in a:
        if b.find(char) != -1:
            return char
    return ""

def shared3(a, b, c):
    for char in a:
        if b.find(char) != -1:
            if c.find(char) != -1:
                return char
    return ""

priorityItems = ""
group = []
badges = ""
cycle = 1
for line in input:
    if line.find("\n") != -1:
        contents = line[:-1]
    else:
        contents = line
    
    pouch1 = contents[:(int)(len(contents)/2)]
    pouch2 = contents[(int)(len(contents)/2):]

    priorityItems += shared(pouch1, pouch2)
#################
    group.append(contents)
    if cycle == 3:
        badges += shared3(group[0], group[1], group[2])
        group = []
        cycle = 1
    else:
        cycle += 1


total = 0
for item in priorityItems:
    if ord(item) > 90:
        total += ord(item) - 96
    else:
        total += ord(item) - 64 + 26

print(total)

total = 0
for item in badges:
    if ord(item) > 96:
        total += ord(item) - 96
    else:
        total += ord(item) - 64 + 26

print(total)