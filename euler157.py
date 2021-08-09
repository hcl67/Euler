'''
易见，当1/a+1/b=p/10**n 是 p = k*l 则 1/ak+1/bk = l/10**n
所以仅需考虑gcd(a,b)=1的情形，此(a,b)*fct(p) 即为所有此a,b对应的解
1. a = 1, b = 2**i*5**j   0<=i,j <= n 
2. a = 2**i b = 5**j      1<=i,j <= n
'''

__f = open("d:\Prime100000.txt", "r")
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

N = 9
ans = []

for n in range(1,N+1):
    ansn = 0
    #1
    for i in range(n+1):
        for j in range(n+1):
            ansn += len(fct(10**n + 2**(n-i)*5**(n-j)))
    #2
    for i in range(1,n+1):
        for j in range(1,n+1):
            ansn += len(fct((2**(n-i)*5**n + 5**(n-j)*2**n)))
    ans += [ansn]
            
print(ans)
print(sum(ans))            
            
        
