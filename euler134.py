import math

__f = open("d:\prime1000000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split(" ")))
__f.close()

__plist += [1000003]
__plist = __plist[2:]

ans = 0


'''
求解丢番图方程：使得
kb%p2 == a
即 kb + mp2 = a
由于p2是质数，所以方程有解，通过扩展欧几里得算法得到解，通过裴蜀定理求的最小S

'''

def gcdplus(a,b):
    if a > b:
        r, nr = a,b
    else:
        r, nr = b,a
        
    s, ns = 1,0
    t, nt = 0,1
    while 1:
        q = r // nr
        r, nr = nr, r%nr
        s, ns = ns, s-q*ns
        t, nt = nt, t-q*nt
        if nr == 0:
            if a > b:
                return r,s,t
            else:
                return r,t,s
        
    

for i in range(len(__plist) - 1):
    p1 = __plist[i]
    p2 = __plist[i+1]
    d = int(math.log10(p1)) + 1
    a = p2 - p1
    b = 10 ** d % p2
    _,m,k = gcdplus(p2,b)
    k = k * a % p2
    n = k*10**d+p1
#    print(p1,n,k,a,b)    
    ans += n
print(ans)
    
