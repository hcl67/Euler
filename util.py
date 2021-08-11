__f = open("prime1000000.txt", "r")
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

def fct(n):
    pfdict = pfdeco(n)
    fct = [1]
    for k,v in pfdict.items():
        kv = [k**i for i in range(v+1)]
        fct = [x*y for x in fct for y in kv]
    return sorted(fct)

    
def gcdplus(a,b):  #生产素勾股数
    if a > b:
        r, nr = a, b
    else:
        r, nr = b, a        
    s, ns = 1, 0
    t, nt = 0, 1
    while 1:
        q = r // nr
        r, nr = nr, r%nr
        s, ns = ns, s-q*ns
        t, nt = nt, t-q*nt
        if nr == 0:
            if a > b:
                return r, s, t
            else:
                return r, t, s
            

def genpgg(thrd):
    from math import gcd
    pgg = []
    for m in range(2,thrd+1):
        for n in range(1,m):
            if gcd(m,n) > 1 or (m+n)%2 == 0:
                continue
            pgg += [(m**2-n**2,2*m*n,m**2+n**2)]
    return pgg            
        
def isprime_mr(n):
    """miller-rabin's prime test"""
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


def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray. Kadane's algorithm"""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum



#时间打点
timestamp = []

def timemark(printflag = False):
    from datetime import datetime
    global timestamp
    ts = datetime.now()
    if len(timestamp) == 0:
        timestamp = [ts]
    else:    
        timestamp[-1] = ts - timestamp[-1]
        timestamp += [ts]
    if printflag:
        for i in range(len(timestamp)-1):
            print(timestamp[i])
        timestamp = []
    return 
        
timemark()
