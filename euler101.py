import math
nlist = []
for n in range(16):
    y = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
#    y = n**3
    nlist.append((n,y))
     
oplist = []

for n in range(1,11):
    for m in range(n+1,n+2):
        sumn = 0
        for i in range(1,n+1):
            prod = nlist[i][1]
            for j in range(1,n+1):
                if j == i:
                    continue
                prod *= (nlist[m][0]-nlist[j][0])/(nlist[i][0]-nlist[j][0])
            sumn += prod
        oplist += [round(sumn)]
print(oplist)
print(sum(oplist))
