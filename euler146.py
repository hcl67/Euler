'''
1. 10|n
2. 3,7,13, 不整除 n


'''

from datetime import datetime 

__f = open("D:\prime10000000.txt", "r")
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
    return dict(pf)

def isprime_mr(n):
    
    if n > 2**64:
        print("warrning, n>2^64, the miller-rabin test may fail")

    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # miller_rabin

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for a in alist:
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True




def check146(n, printflag = True):
    for j in [1,3,7,9,13,27]:
        if not isprime_mr(n**2+j):
            if printflag:
                print(n,"** 2 +",j,'非质数:')
                #print(n**2+j,"分解：",dict(pfdeco(n**2+j)))
            return False
    for j in [11,17,19,21,23]:
        if isprime_mr(n**2+j):
            if printflag:
                print(n,"** 2 +",j,'质数:')
            return False
    return True

btime = datetime.now()

ans = []

for n in range(10,150000000,10):
    if n%3 == 0 or n%7 in {0,1,2,5,6} or n%11 in {2,9} or n%13 in {0,2,5,6,7,8,11} or n%17 in {2,4,5,12,13,15}:
        continue
    if check146(n,False):
        print(n)
        ans += [n]

print(sum(ans))
print(datetime.now() - btime)
