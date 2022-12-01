input = open("dec1/day1.txt", "r")
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

list.sort(reverse= True)

print("max calories carried:", list[0])
print("calories carried by top 3:", (list[0] + list[1] + list[2]))