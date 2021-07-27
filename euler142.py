
'''
x-z = x-y + y-z
x+z = x-y + y+z
x+y = x-z + y+z

设:
x-y = a^2
y-z = b^2
x-z = c^2
y+z = d^2
x+z = e^2
x+y = f^2

a^2 + b^2 = c^2
a^2 + d^2 = e^2
c^2 + d^2 = f^2

可解得：
x = a^2 + (b^2 + d^2)/2
y = (d^2 + b^2)/2
z = (d^2 - b^2)/2
满足 x > y > z > 0
d > b

x+y = a^2 + d^2 + b^2

令

1)
a = 2m1n1 = 2m2n2  m1>n1 m2>n2
b = m1^2 - n1^2
c = m1^2 + n1^2
d = m2^2 - n2^2
e = m2^2 + n2^2

x+y = m1^4 + n1^4 + m2^4 + n2^4 要是完全平方数

未必最优解

2)
考虑生产一大波素勾股数，然后
i) LCM(a,d)//a = s, LCM(a,d)//d = t, as = dt
 验证 as^2+bs^2+et^2
ii) LCM(a,e)//a = s, LCM(a,e)//e = t, as = et
 验证 as^2+bs^2+dt^2
iii) LCM(b,d)//b = s, LCM(b,d)//d = t, bs = dt
 验证 as^2+bs^2+et^2
iv) LCM(b,e)//b = s, LCM(b,e)//e = t, bs = et
 验证 as^2+bs^2+dt^2
 
4种场景寻找最小值


'''

  
__f = open("d:\prime1000000.txt", "r")
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



from datetime import datetime
from math import isqrt,gcd

btime = datetime.now()



def genpgg(thrd):
    from math import gcd
    pgg = []
    for m in range(2,thrd+1):
        for n in range(1,m):
            if gcd(m,n) > 1 or (m+n)%2 == 0:
                continue
            pgg += [(m**2-n**2,2*m*n,m**2+n**2)]
    return pgg

gglist = genpgg(100)
        
pp = 99999999
xx,yy,zz=0,0,0
for i in range(1,len(gglist)-1):
    for j in range(i):
        for k in range(4):
            if k == 0: #i
                x1,y1,z1 = gglist[i]
                x2,y2,z2 = gglist[j]
            elif k == 1:
                y1,x1,z1 = gglist[i]
                x2,y2,z2 = gglist[j]
            elif k == 2:
                x1,y1,z1 = gglist[i]
                y2,x2,z2 = gglist[j]
            elif k == 3:
                y1,x1,z1 = gglist[i]
                y2,x2,z2 = gglist[j]
            g = gcd(x1,x2)
            s = g*x2
            t = g*x1
            n = (x1*s)**2+(y1*s)**2+(y2*t)**2
            if isqrt(n)**2 == n:
                a = x1*s
                b = min(y1*s,y2*t)
                d = max(y1*s,y2*t)
                x = a**2 + (b**2 + d**2)/2
                y = (d**2 + b**2)/2
                z = (d**2 - b**2)/2
                if x+y+z<pp:
                    xx,yy,zz = int(x),int(y),int(z)
                    pp = xx+yy+zz
                    print(xx,yy,zz,pp)

print(xx,yy,zz,pp)
'''
未必最优解
pp = 99999999
xx,yy,zz=0,0,0

for n in range(2,10000):
    fctlist = fct(n)
    ln = len(fctlist)
    if ln < 4:
        continue
    for i in range(1,ln//2):
        for j in range(0,i):
            t = fctlist[i]**4+fctlist[j]**4+fctlist[ln-1-i]**4+fctlist[ln-1-j]**4
            if isqrt(t)**2 == t:
                m1 = fctlist[ln-1-i]
                n1 = fctlist[i]
                m2 = fctlist[ln-1-j]
                n2 = fctlist[j]
                a = 2*m1*n1
                b = m1**2 - n1**2
                d = m2**2 - n2**2
                x = a**2 + (b**2 + d**2)/2
                y = (d**2 + b**2)/2
                z = (d**2 - b**2)/2
                if x == int(x) and y == int(y) and z == int(z) :
                    print(int(x),int(y),int(z))
                    if x+y+z<pp:
                        xx,yy,zz = int(x),int(y),int(z)
                        pp = xx+yy+zz
        
print(xx,yy,zz,pp)
'''



print(datetime.now()-btime)
