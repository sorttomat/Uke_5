infile = open("fil_med_navn.txt", "r")
lines = infile.readlines()

mennesker = []
hunder = []

for line in lines:
    line = line.strip("\n")
    line = line.split(" ")
    if line[0] == "H":
        hunder.append(line[1])
    else:
        mennesker.append(line[1])
infile.close()
print(mennesker, hunder)

