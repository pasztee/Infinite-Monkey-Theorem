import random as rn
f = open("ref.txt", "r")
characters = []
chance = []
for line in f:
    s,t=map(float,line.split(";"))
    characters.append(int(s))
    chance.append(t)
f.close()
output = []
randomnumber = 0
lines = int(input('Number of lines>>'))
charPerLin = int(input('Characters per line>>'))
f = open("monkey.txt", "a", encoding="utf-8")
while lines > 0:
    output = rn.choices(characters, weights=chance, k=charPerLin)
    #print(output)
    for x in output:
        f.write(chr(x))
    f.write('\n')
    lines -= 1
    output.clear()
f.close()
print('end')
#print(characters, chance)