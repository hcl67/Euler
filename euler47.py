'''
Project Euler Problem #47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2*7
15 = 3*5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2*7*23
645 = 3*5*43
646 = 2*17*19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
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

i=1
while 1:
    if len(set(Pfctr(i)))==4 and len(set(Pfctr(i+1)))==4 and len(set(Pfctr(i+2)))==4 and len(set(Pfctr(i+3)))==4:
        print(i,i+1,i+2,i+3)
        break
    i+=1
       
