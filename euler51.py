'''
Project Euler Problem #51

By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
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

def genPrime():
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

def checkpb(p,b):
    pcount=0  ##record maximum number of prime value family
    for i in range(10):
        t=''  ##possible prime value
        if b[0]=='1' and i==0: continue ##skip the first digit 0
        for j in range(len(b)):
            if b[j]=='1':
                t+=str(i)
            else:
                t+=p[j]
        if isPrime(int(t)):
            pcount+=1
    return pcount

def decomBin(s):  ##numerate the possible combination of 1's from s
    count=s.count('1')  ## count number 1's from s
    db=[bin(i)[2:] for i in range(1,2**count)]
    db2=[]
    for i in db:
        while len(i)<count:
            i='0'+i
        db2.append(i)
    ds=[]
    for i in range(2**count-1):
        news=''
        dbi=0 ##counter for permutation
        for j in range(len(s)):
            if s[j]=='0':
                news+='0'
            else:
                news+=db2[i][dbi]
                dbi+=1
        ds.append(news)
    return ds

def checkp(p):
    strp=str(p)
    for i in range(3):  ##loop for 0,1,2
        if strp.count(str(i))==0: continue
        strbin=''
        for j in range(len(strp)):
            if strp[j]==str(i):
                strbin+='1'
            else:
                strbin+='0'
        strcombin=decomBin(strbin)
        for k in range(len(strcombin)):
            pcount=checkpb(strp,strcombin[k])
            if pcount>=8:
                print(strp)
                return True
    return False

def find():
    for p in genPrime():
        if p<56993: continue
        if checkp(p): return

find()            













    
