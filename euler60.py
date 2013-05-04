'''
Project Euler #60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

from math import sqrt
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

def check(s,p):
    for i in s:
        if isPrime(int(str(i)+str(p))) and isPrime(int(str(p)+str(i))): continue
        else: return False
    return True

primel1m1=[[3]]
primel1m2=[[3]]
primel2m1=[]
primel2m2=[]
primel3m1=[]
primel3m2=[]
primel4m1=[]
primel4m2=[]
primel5m1=[]
primel5m2=[]


def findp():
    maxp=99999;
    j=1
    for i in genPrime():
        if i>j*500:
            print(i)
            print(maxp)
            j+=1
        if i>maxp:
            print(maxp)
            print(primel5m1)
            print(primel5m2)
            return
        if i<=3:
            continue
        elif i%3==1:
            for s in primel4m1:
                if check(s,i):
                    primel5m1.append(s+[i])
                    maxp=min(maxp,sum(s)+i)
            for s in primel3m1:
                if check(s,i):
                    primel4m1.append(s+[i])
            for s in primel2m1:
                if check(s,i):
                    primel3m1.append(s+[i])
            for s in primel1m1:
                if check(s,i):
                    primel2m1.append(s+[i])
            primel1m1.append([i])
        else:
            for s in primel4m2:
                if check(s,i):
                    primel5m2.append(s+[i])
                    maxp=min(maxp,sum(s)+i)
            for s in primel3m2:
                if check(s,i):
                    primel4m2.append(s+[i])
            for s in primel2m2:
                if check(s,i):
                    primel3m2.append(s+[i])
            for s in primel1m2:
                if check(s,i):
                    primel2m2.append(s+[i])
            primel1m2.append([i])
findp()
