from math import prod,isqrt,gcd  
from datetime import datetime
from sortedcontainers import SortedList

btime = datetime.now()

f = open("d:\prime1000000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()

def pfdeco(n):
    if n == 1:
        return [1]
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


    

    
def rad127(n):
    return prod(set(pfdeco(n)))

thrd = 120000

ans = []
 

radlist = [0]

for i in range(1,thrd+1):
    radlist += [rad127(i)]
    
from collections import defaultdict    
iraddict = defaultdict(list)
for i in range(1,thrd+1):
    iraddict[radlist[i]] += [i]
    
for c in range(5,thrd+1):
    for r in range(1,c//radlist[c]+1):
        for a in iraddict[r]:
            if a > c//2:
                continue
            b = c-a
            if radlist[a] * radlist[b] * radlist[c] < c and gcd(a,b) == 1:
                ans += [(a,b,c)]
            
        

    
'''  
for c in range(5,thrd):
#    print(c)
    cradset = set(pfdeco(c))
    crad = prod(cradset)
    radabmax = c // crad
    if radabmax <= 2:
        continue

    pf = sorted(list(set(filter(lambda x: x <= radabmax,plist[:radabmax])).difference(cradset)))

    
    if len(pf) == 0:
        continue
    elif len(pf) == 1 or pf[0]*pf[1] > radabmax:
        if rad127(c-1) * crad < c:
            ans += [(1,c-1,c)]
    else:

        ablist = SortedList([1])
        for p in pf:
            np = p
            while np < c:
                ablistupd = []
                for b in ablist:
                    if b*np > c:
                        break
                    else:
                        ablistupd += [b*np]
                ablist.update(ablistupd)
                np *= np
                                
        if len(ablist)<2:
            continue
        ai = 0
        bi = len(ablist)-1
        while ai < bi:
            a = ablist[ai]
            b = ablist[bi]
            if a+b<c:
                ai += 1
            elif a+b>c:
                bi -= 1
            elif gcd(a,b) == 1 and rad127(a) * rad127(b) * crad < c:
                ans += [(a,b,c)]
                ai += 1
            else:
                ai += 1
           



for c in range(2,thrd):
#    print(c)
    cradset = set(pfdeco(c))
    crad = prod(cradset)
    if c // crad <= 2:
        continue
    for a in range(1,c//2):
        aradset = set(pfdeco(a))
        if len(set.intersection(aradset, cradset))>0:
            continue
        b = c - a
        bradset = set(pfdeco(b))
        if len(set.intersection(bradset, cradset))>0 or len(set.intersection(bradset, aradset))>0:
            continue
        if prod(aradset) * prod(bradset) * crad < c:
            ans += [(a,b,c)]
  
'''             
             


            
print(len(ans),sum([x[2] for x in ans]))
print(datetime.now()-btime)



        
    
