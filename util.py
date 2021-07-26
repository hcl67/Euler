__f = open("prime100000.txt", "r")
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

    
def gcdplus(a,b):
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
        
