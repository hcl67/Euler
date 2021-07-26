from datetime import datetime
from math import sqrt

btime = datetime.now()


__f = open("d:\prime100000000.txt", "r")
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

def isprime(n):
    if n == 1:
        return False
    if n < 1000000:
        if n in __pset:
            return True
        else:
            return False
    for p in __plist:
        if p*p>n:
            break
        elif n%p == 0:
            return False
    return True



'''
(x+b)^2-x^2-(x-b)^2 = S => (4b-x)*x = S
若 S=xy 则 b = (x+y)/4
因 x>b => 当 y/x > 3 or x < sqrt(n/3) 时只有1解。
考虑 x=y 时，则有 x=y=2k =>若k是奇数则 4|(2+2k^2)，若k是偶数则4|(4+k^2),故完全平方数不可能只有1组 x=y的解(k=1,2除外)


分类分析:
16*2k >1解
16p p>=3质数or1 1解 
16p1p2 p1,p2>=3的奇数 >1解
8*(2k-1) 无解
4p p>=3质数 1解
4p1p2 p1,p2>=3的奇数 >1解
2*(2k-1) 无解
4k+1 无解
4k+3 是合数 >1解
4k+3 是质数 1解

于是发现 1解为p：[4,16] + [p%4==3] + [4p] + [16p] p>=3 
'''
thrd = 50000000

ans = [4,16]



for p in __plist:
    if p <= 2:
        continue
    if p > thrd:
        break
    if p%4 == 3:
        ans += [p]
    if 4*p < thrd:
        ans += [4*p]
    if 16*p < thrd:
        ans += [16*p]
        
            


print(len(ans))

print(datetime.now()-btime)
