__f = open("d:\prime1000000.txt", "r")
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


'''
r<d:

1. r d q
2. r q d
3. q r d

设公比p，p>1

1.2. 本质一致  n = t^2 = r^2*p^3 + r
3. n = t^2 = r^2 + r 无解    

r * t^2 = (r*p)^3 + r^2
令 r*p = d
则 r | d^2 (q是整数)

22min...

'''
from datetime import datetime
from math import isqrt

btime = datetime.now()
thrd = 1000000
thrd2 = thrd**2

ans = []
for d in range(1,thrd+1):
    d2 = d**2
    rlist = fct(d2)
    rn = len(rlist)
    ind = rn//2
    for i in range(ind-1,-1,-1):
        t2 = rlist[i] + rlist[rn-1-i]*d
        if t2 > thrd2:
            break
        t = isqrt(t2)
        if t*t == t2:
            print(t*t,rlist[i],d)
            ans += [(t*t,rlist[i],d)]
            
ans.sort()            
print(ans)
print(sum(map(lambda x:x[0],ans)))
print(datetime.now()-btime)
