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
    


使用 ke9tv 的思路，设p = a/b  a>b gcd(a,b) = 1

则 d = a*r/b; q = a^2*r/b^2

b^2 | q => r = c*b^2, q = a*c*b, d = a^2*c

n = dq+r = a^3*b*c^2 + c*b^2.



'''
from datetime import datetime
from math import isqrt,gcd

btime = datetime.now()

ans = set()

for a in range(1,10000+1):
    for b in range(1,a):
        if gcd(a,b)>1:
            continue
        if (a**3)*b+(b**2)>=1e12:
            break
        c = 0
        while 1:
            c += 1
            n = a**3*b*c**2 + c*b**2
            if n > 1e12:
                break
            if isqrt(n)**2 == n:
                print(n)
                ans.add(n)
print(ans)
print(sum(ans))


'''
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
'''  
print(datetime.now()-btime)
