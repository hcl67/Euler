f = open("prime100000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()

def isprime(n):
    if n == 1:
        return False
    for p in plist:
        if p*p>n:
            break
        elif n%p == 0:
            return False
    return True
  
def pfdeco(n):
    pf = []
    pn = 0
    p = plist[pn]
    while n>1:
        if n%p == 0:
            pf += [p]
            n //= p
        else:
            pn += 1
            p = plist[pn]
    return pf
    
    
def gcd(a,b):
    if a>b:
        a,b = b,a
    c = b%a
    if c == 0:
        return a
    else:
        return gcd(c,a)    
