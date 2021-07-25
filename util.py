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
                return nr,s,t
            else:
                return nr,t,s
        
