
__f = open("d:\prime1000000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split(" ")))
__f.close()

def isprime(n):
    if n == 1:
        return False
    for p in __plist:
        if p*p>n:
            break
        elif n%p == 0:
            return False
    return True

from math import gcd

def pfdeco(n):
    pf = []
    pn = 0
    p = __plist[pn]
    while n>1:
        if n%p == 0:
            pf += [p]
            n //= p
        else:
            pn += 1
            p = __plist[pn]
    return pf



thrd = 200000

def A132(n):
    if gcd(n,10) > 1:
        return -1
    sumr = 1
    cr = 1
    k = 1
    while sumr % n != 0:
        cr  = cr * 10 % n
        sumr += cr
        k += 1
    return k



pdet = {}
for p in __plist:
    pdet[p] = A132(p)
    if p > thrd:
        break

'''
若p|R(k),则 R(A(p))|R(k) (若不然 R(k) % R(A(p)) = R(t) < R(A(p)), 则有 p | R(t) 与A(p)的定义不符)
又 R(t)|R(k) <=> t|k 
=> p|R(k) <=> A(P)|k
故变为寻找A(p)|k的p


'''
ans = []
for p in __plist:
    if p == 2 or p == 5:
        continue
        
    if 10**9 % pdet[p] == 0:
        ans += [p]
        print(p)
    if len(ans) >= 40:
        break
print(len(ans), sum(ans[:40]))

