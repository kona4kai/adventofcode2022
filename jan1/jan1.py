input = open("jan1/day1.txt", "r")
list = []

elfTotalCal = 0
for line in input:
    if line == "\n":
        list.append(elfTotalCal)
        elfTotalCal = 0
    else:
        elfTotalCal = elfTotalCal + int(line.replace("\n", ""))

if elfTotalCal != 0:
    list.append(elfTotalCal)

mostCal = 0
secondMostCal = 0
thirdMostCal = 0
for item in list:
    if item >= mostCal:
        thirdMostCal = secondMostCal
        secondMostCal = mostCal
        mostCal = item
    elif item >= secondMostCal:
        thirdMostCal = secondMostCal
        secondMostCal = item
    elif item >= thirdMostCal:
        thirdMostCal = item
        

top3 = mostCal + secondMostCal + thirdMostCal

print("max calories carried:", mostCal)
print("calories carried by top 3:", top3)