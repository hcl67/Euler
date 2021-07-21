f = open("prime100000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()


def pfdeco(n):
    pf = []
    pn = 0
    p = plist[pn]
    while n>1:
        if n%p == 0:
            pf += [p]
            n //= p
        else:
            pn += 1
            p = plist[pn]
    return pf
    

from math import prod

k = 100000
ans = 10000
rad = [1,2,3]

def rad124(n):
    return prod(set(pfdeco(n)))

for n in range(4,k+1):
    rad += [rad124(n)]



print(sorted(list(range(1,k+1)),key = lambda x:rad[x-1])[ans-1])
