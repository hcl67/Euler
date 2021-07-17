from itertools import combinations
f = open("D:\prime100000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()


_s = 10

def isprime111(n):
    for p in plist:
        if n%p == 0:
            return False
    return True

def gennum111(d,k):
    pdklist = []
    base = str(d)*_s
    poslist = combinations(list(range(10)),k)
    for pos in poslist:
        for j in range(10**k):
            num = list(base)
            sj = str(j).zfill(k)
            if str(d) in sj:
                continue
            for l in range(k):
                num[pos[l]] = sj[l]
            num = int(''.join(num))
            if num < 1000000000:
                continue
            if isprime111(num):
                pdklist += [num]
    return pdklist

k = [[] for i in range(10)]
for i in range(10):
    d = 1
    ki = gennum111(i,d)
    while(len(ki) == 0):
        d+=1
        ki = gennum111(i,d)
    k[i] = ki
                
print(sum([sum(ki) for ki in k]))
