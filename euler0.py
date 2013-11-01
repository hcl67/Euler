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
            s.append(i)
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




def Triangle(n):
    return n*(n+1)/2

def calTriangle(x):
    return (math.sqrt(1+8*x)-1)/2

def isTriangle(x):
    n = calTriangle(x)
    return n==int(n)

def Square(n):
    return n*n

def calSquare(x):
    return math.sqrt(x)

def isSquare(x):
    n = calSquare(x)
    return n==int(n)

def Pentagonal(n):
    return n*(3*n-1)/2

def calPentagonal(x):
    return (math.sqrt(1+24*x)+1)/6

def isPentagonal(x):
    n = calPentagonal(x)
    return n==int(n)

def Hexagonal(n):
    return n*(2*n-1)

def calHexagonal(x):
    return (math.sqrt(1+8*x)+1)/4

def isHexagonal(x):
    n = calHexagonal(x)
    return n==int(n)

def Heptagonal(n):
    return n*(5*n-3)/2

def calHeptagonal(x):
    return (math.sqrt(9+40*x)+3)/10

def isHeptagonal(x):
    n = calHeptagonal(x)
    return n==int(n)

def Octagonal(n):
    return n*(3*n-2)

def calOctagonal(x):
    return (math.sqrt(4+12*x)+2)/6

def isOctagonal(x):
    n = calOctagonal(x)
    return n==int(n)

def Permutate(l):   ##generate all permutation of list l
    if len(l)==1:
        return [l]
    else:
        returnlist=[]
        for i in range(len(l)):
            t=[x for x in l]
            t.pop(i)
            p=Permutate(t)
            for j in p:
                returnlist+=[[l[i]]+j]
        return returnlist

def calDigt(s):
    n=0
    for i in s:
        n+=int(i)

    return n
