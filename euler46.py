'''
Project Euler Problem #46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1**2
15 = 7 + 2*2**2
21 = 3 + 2*3**2
25 = 7 + 2*3**2
27 = 19 + 2*2**2
33 = 31 + 2*1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
from math import sqrt
from math import ceil
def isPrime(x):
    if x%2==0 and x!=2:
        return 0
    else:
        for i in range(3,int(sqrt(x))+1,2):
            if x%i==0 and x!=i:
                return False
        return True

def genOddComposite(k=3):
    n=k
    while 1:
        if not isPrime(n):
            yield n
        n+=2

def check(n):
    for i in range(1,ceil(sqrt(n/2))):
        if isPrime(n-2*i*i):
            return True
    return False
    

def find():
    for i in genOddComposite():
        if not check(i):
            print(i)
            return
    
find()
