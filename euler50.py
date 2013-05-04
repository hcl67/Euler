'''
Project Euler Problem #50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

prime=[2]
x=3
while x<=1000000:
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
    x+=2

n=0
s=0
while s<1000000:
    s+=prime[n]
    n+=1
print(n)

def find():
    lp=len(prime)
    for i in range(n-1,0,-1):
        for j in range(lp-i):
            s=sum(prime[j:i+j])
            if s>1000000: break
            if isPrime(s):
                print(s)
                return

find()
