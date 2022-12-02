#returns points for combo
def points(opp, you):
    points = 0
    if you == 'X':
        points += 1
        if opp == 'A':
            points += 3
        elif opp == 'C':
            points += 6
    elif you == 'Y':
        points += 2
        if opp == 'B':
            points += 3
        elif opp == 'A':
            points += 6
    else:
        points += 3
        if opp == 'C':
            points += 3
        elif opp == 'B':
            points += 6
    return points

#returns points based on outcome
def points2(opp, outcome):
    points = 0
    if outcome == 'X':
        if opp == 'A':
            points += 3
        elif opp == 'B':
            points += 1
        else:
            points += 2
    elif outcome == 'Y':
        points += 3
        if opp == 'A':
            points += 1
        elif opp == 'B':
            points += 2
        else:
            points += 3
    else:
        points += 6
        if opp == 'A':
            points += 2
        elif opp == 'B':
            points += 3
        else:
            points += 1
    return points

#main program
input = open("dec2/day2.txt", "r")

totalPoints = 0
totalPoints2 = 0
for line in input:
    totalPoints += points(line[0], line[2])
    totalPoints2 += points2(line[0], line[2])
    
print(totalPoints)
print(totalPoints2)





