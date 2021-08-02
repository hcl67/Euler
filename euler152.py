

__f = open("d:\prime1000000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split()))
__f.close()
__pset = set(__plist)

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

def maxpf(n):
    d = dict(pfdeco(n))
    p = max(d.keys())
    return p,d[p]

from itertools import combinations
from math import isqrt,prod,gcd,log
from functools import reduce

l = list(range(1,10))

N = 80

def lcm(x,y):
    return x*y//gcd(x,y)

def genn4p(pl,N):
    ans = [1]
    for p in pl:
        np = []
        k = 1
        while k < N:
            np += [k]
            k *= p
        ans = [x*y for x in ans for y in np if x*y < N]
    ans.remove(1)
    return sorted(ans)
    

def check152(nums):
    nums = [x**2 for x in nums]
    d = reduce(lcm, nums)
    n = sum(d//x for x in nums)
    g = gcd(n,d)  #先约分
    g = prod(gp**(gpn//2*2) for gp,gpn in pfdeco(g).items())
    n//=g
    d//=g
    return n,d
                
def cal152(rn = 0,rd = 1, nums = [], pl = [], N = N): 
    '''
    换个思路，给定余数开始，在thrd下，nums不重复的前提下，消除除2外的所有余数
    '''
    p,np = maxpf(rd)
    np//=2
    
    if p == 2:
        return [(rn,rd,nums)]
    l = genn4p(pl,N)
    l = [x**2 for x in l if x%p==0]
    ans = []
    for n in range(1,len(l)):
        for k in combinations(l, n):
            ssd = reduce(lcm,k) #通分后的分母，不含引入的余数项
            ssn = sum(ssd//i for i in k) #通分后的分子，不含引入的余数项
            tssd = ssd * rd      #含余数后的分母
            tssn = ssn * rd + rn * ssd #含余数后的分子
            g = gcd(tssn,tssd)  #先约分
            g = prod(gp**(gpn//2*2) for gp,gpn in pfdeco(g).items())
            tssn//=g
            tssd//=g
            if tssd % (p**2) > 0:
                newnums = [isqrt(x) for x in k]
                ans += [(tssn,tssd,sorted(nums+newnums),[x for x in pl if x != p])]
    return ans           
         



def warp152(rn,rd,nums):
    l = [4**n for n in range(int(log(rd,4)))]
    for n in range(1,len(l)+1):
        for ll in combinations(l, n):
            if rn+sum(ll) == rd//2:
                return sorted([isqrt(rd//x) for x in ll]+nums)
    return []
    

N = 80

check = []
ansd = {}
for n in range(3,N+1):
    if n in {4,8,16,32,64}:
        continue
    print(n)
    paral = [(1,n**2,[n],[2,3,5,7,11,13])]

    while len(paral) > 0:
        newparal = []
        for rn,rd,nums,pplist in paral:
            if maxpf(rd)[0] == 2:
                check += [(n,tuple(nums),rn,rd)] 
                ansd[tuple(nums)] = (rn,rd)
            else:
                newparal += cal152(rn,rd,nums,pplist,n)
        paral = newparal

        
#print(cal152(1, 12**2, [15, 20],20))

#print(cal152(1, 35**2, [35],35)  )  
while 1:
    patchdict = {}
    for x in ansd.keys():
        for y in ansd.keys():
            if x == y:
                continue
            if len(set(x).intersection(set(y))) == 0:
                z = tuple(sorted(list(set(x).union(set(y)))))
                if z not in ansd.keys():
                    rn1,rd1 = ansd[x]
                    rn2,rd2 = ansd[y]
                    rd = lcm(rd1,rd2)
                    rn = rd//rd1*rn1+rd//rd2*rn2
                    patchdict[z] = (rn,rd)
    if len(patchdict) == 0:
        break
    else:
        print(len(patchdict))
        ansd.update(patchdict)

ans = []
                
for k,v in ansd.items():
   
    rn,rd = v
    aaa = warp152(rn,rd,list(k))
    if len(aaa)>0:
        ans += [aaa]

print(ans)
print()
print(len(ans))               


'''
'''
