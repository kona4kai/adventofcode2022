input = open("dec5/input.txt", "r")
crates = ["","JHPMSFNV","SRLMJDQ","NQDHCSWB","RSCL","MVTPFB","TRQNC","GVR","CZSPDLR","DSJVGPBF"]

print(crates)
for line in input:
    num = line[5:line.find(" ", 5)]
    old = line[11+len(num):line.find(" ", 11+len(num))]
    new = line[15+len(num)+len(old):-1]
    num = int(num)
    old = int(old)
    new = int(new)
    crates[new] = crates[new] + crates[old][num*-1:]
    crates[old] = crates[old][:num*-1]

out = "top: "
for item in crates[1:]:
    out = out + item[-1:]
print(out)