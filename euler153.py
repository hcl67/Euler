 # 一个半小时版本，再想想
__f = open("d:\prime100000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split()))
__f.close()
__pset = set(__plist)

  
def pfdeco(n):
    from collections import defaultdict
    pf = defaultdict(int)
    pn = 0
    p = __plist[pn]
    while n>1:
        if n%p == 0:
            pf[p] += 1
            n //= p
        elif p*p > n:
            pf[n] += 1
            break
        else:
            pn += 1
            p = __plist[pn]
    return pf

def fct(n):
    pfdict = pfdeco(n)
    fct = [1]
    for k,v in pfdict.items():
        kv = [k**i for i in range(v+1)]
        fct = [x*y for x in fct for y in kv]
    return sorted(fct)

from math import gcd,isqrt,prod
from collections import defaultdict
from datetime import datetime
from functools import reduce

time0 = datetime.now()

N = 10**5

'''
实数部分有 n = p1^n1 *...* pk^nk => S(n) = S(p1^n1)*...*S(pk^nk) = (p1^(n1+1)-1)/(p1-1) *...* (pk^(nk+1)-1)/(pk-1)

虚数部分找可进一步分解的[pi],再组合

'''
ccdict = defaultdict(int)

for i in range(1,isqrt(N)+1):
    for j in range(1,min(i,isqrt(N - i**2))+1):
        if gcd(i,j) == 1:
            if i == j:
                ccdict[i**2+j**2] += (i)*2
            else:
                ccdict[i**2+j**2] += (i+j)*2

time1 = datetime.now()

tot = [0,1]

dddict = {1:1}
ctdict = {}

for i in range(2,N+1):
    pfi = pfdeco(i)
    sfi = prod((p**(n+1)-1)//(p-1) for p,n in pfi.items())
    dddict[i] = sfi
    toti = sfi
    ipfi = [[p**i for i in range(n+1)] for p,n in pfi.items() if p in ccdict]

    if len(ipfi) > 0:
        ifi = reduce(lambda x,y:[xi*yi for xi in x for yi in y],ipfi)
        for f in ifi:
            if f in ccdict:
                toti += ccdict[f]*dddict[i//f]
    
    # fi = fct(i)
    # sfi = sum(fi)
    # dddict[i] = sfi
    # toti = sfi
    # for f in fi:
    #     if f in ccdict:
    #         toti += ccdict[f]*dddict[i//f]
    ctdict[i] = toti-dddict[i]
    tot += [toti]

print(sum(tot))
print(time1-time0,datetime.now()-time1)
