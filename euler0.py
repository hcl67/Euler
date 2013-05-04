'''
Save all useful function for future usage
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

def genPrime(): ##gen prime
    prime=[2]
    x=1
    while 1:
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

def isTriangle(n): ##check if n is triangle number (=n(n+1)/2)
    k=int(sqrt(n*2))
    return k*(k+1)==n*2

def isPentagonal(n): ##check if n is pentagonal number (=n(3n-1)/2)
    k=ceil(sqrt(n*2/3))
    return k*(3*k-1)==n*2

def isHexagonal(n):  ##check if n is hexagonal number (=n(2n-1))
    k=ceil(sqrt(n/2))
    return k*(2*k-1)==n

def HCF(a,b):  ##find the highest common factor of a,b
    x=max(a,b)
    y=min(a,b)
    while x%y!=0:
        t=x%y
        x=y
        y=t
    return y

def fctr(n): ##find all factors of n
    k=n//2+1
    s=[]
    for i in range(1,k):
        if n%i==0:
            s.append(n)
    return s

def Pfctr(n):  ##find all prime factors of n
    k=n
    s=[]
    while not isPrime(k):
        for i in range(2,int(sqrt(k))+1):
            if k%i==0:
                s.append(i)
                k=k//i
                break
    s.append(k)
    return s

def permu(a,b): ##find all permutation of p using permu('',p)
    if len(b)==0:
        print(a)
    else:
        for i in b:
            c=b[:b.index(i)]+b[b.index(i)+1:]
            permu(a+i,c)

def lettlecomp(a,b): ##compare the difference of letters from 2 strings
    return ''.join(sorted(list(str(a)))) == ''.join(sorted(list(str(b))))


def fmtz(i,n):  ##add '0' before integer i till length of n
    k=str(i)
    if len(k)>=n:
        return k
    else:
        while len(k)<n:
            k='0'+k
        return k
