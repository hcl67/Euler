# -*- coding: cp936 -*-
'''
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

Hint

Pell equation, wikipedia
'''

from math import sqrt
from math import ceil
import math

def isqrt(n):
    x=float(n)
    while 1:
        y=x
        x=(y+n/y)/2
        if y-x<1:
            break
    return int(x)


def isSquare(x):
    return sqrt(x)==int(sqrt(x))



'''

l_d=[x for x in range(1,1001) if not isSquare(x)]

y=1
while len(l_d)>1:
    lenl_d=len(l_d)
    for d in l_d:
        if d%10 in [1,2,6,7] and y%10 in [1,9,4,6]:
            continue
        elif d%10 in [3,4,8,9] and y%10 in [2,8,3,7]:
            continue
        x2=y*y*d+1
        if (isqrt(x2)**2-y*y*d==1):
            print(d,isqrt(x2),y)
            l_d.pop(l_d.index(d))
#            print(d,(l_d))

    if lenl_d!=len(l_d):
        print("len(l_d)=",len(l_d))
    y+=1
print(l_d)
'''
nmax=1000000
def conFrac1(n,nmax):
    a1=int(sqrt(n))
    a2=a1
    a3=1
    res=[a1]
    i=1
    while i<=nmax:
        r=[t for t in res]
        yield r   ##yield would release the content of yielded var.
        #print(seq)
        b1=a1
        b2=a2
        b3=a3
        a1=int(b3/(sqrt(n)-b2))
        a3=(n-b2*b2)/b3
        a2=a1*a3-b2
        res.append(a1)
        i+=1

def calFrac1(x):
    a=1
    b=x.pop(-1)
    while(len(x)>0):
        c=x.pop(-1)
        a+=b*c
        t=b
        b=a
        a=t
    return [b,a]

l_d=[x for x in range(1,1001) if not isSquare(x)]

maxx=0
maxd=0

for d in l_d:
    for l in conFrac1(d,nmax):
        #print("l =",l)
        frac=calFrac1(l)
        #print("frac =",frac)
        x=frac[0]
        y=frac[1]
        if x*x-d*y*y==1:
            #print("d =",d,"x =",x,"y =",y)
            #print("x*x =",x*x)
            #print("d*y*y =",d*y*y)
            if x>maxx:
                maxx=x
                maxd=d
            break

print("max x =",maxx)
print("d =",maxd)
