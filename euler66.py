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
'''

from math import sqrt
from math import ceil
def isPrime(x): ##check if x is prime
    if x<1:
        return False
    if x%2==0 and x!=2:
        return False
    else:
        for i in range(3,int(sqrt(x))+1,2):
            if x%i==0 and x!=i:
                return False
        return True

def genPrime(nmax): ##gen prime
    prime=[2]
    x=1
    while x<nmax:
        x+=2
        flg=0
        sqx=int(sqrt(x))
        for d in prime:
            if x%d==0:
                flg=1
                break
            if d>sqx:
                break
        if flg==0:
            prime.append(x)
            yield x

def isSquare(x):
    return sqrt(x)==int(sqrt(x))

l_d=[]
for d in genPrime(1000):
    l_d.append(d)
s=1
while len(l_d)>1:
    lenl_d=len(l_d)
    s2=s*s
    for d in l_d:
        s2d=s2*d
        if isSquare(s2d+2) or isSquare(s2d-2) or isSquare(s2d-1) or isSquare(s2d+1):
            #print(d)
            l_d.pop(l_d.index(d))
    if lenl_d!=len(l_d) and len(l_d)%10==0:
        print(len(l_d))
    s+=1
print(l_d)

