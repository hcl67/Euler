'''
Project Euler Problem #41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import math
def isprime(x):
    if x%2==0 and x!=2:
        return 0
    else:
        for i in range(3,int(math.sqrt(x)),2):
            if x%i==0 and x!=i:
                return 0
        return 1

def permu(a,b):
    if len(b)==0:
        if isprime(int(a))==1:
            slst.append(int(a))
    else:
        for i in b:
            c=b[:b.index(i)]+b[b.index(i)+1:]
            permu(a+i,c)

p='987654321'
slst=[]

while len(p)>1:
    permu('',p)
    if len(slst)>0:
        print(max(slst))
        break
    else:
        p=p[1:]

        
