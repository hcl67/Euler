f = open("D:\p099_base_exp.txt", "r")
numlist = []
for line in f:
    numlist += [tuple(map(int,line.rstrip("\n").split(",")))]
f.close()

maxind = 0

for tp in range(1,len(numlist)):
    b1 = numlist[maxind][0]
    p1 = numlist[maxind][1]
    b2 = numlist[tp][0]
    p2 = numlist[tp][1]
    if pow(b1,p1/p2) < b2:
        maxind = tp
print(maxind+1)
