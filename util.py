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
    
