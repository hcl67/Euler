'''
Project Euler Problem #37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

slst=[]
p=[[3,7]]
d=1
m=[1,3,7,9]
h=[2,3,5,7]
while 1:
    if len(p[-1])==0:
        break
    tmp1=[hi*(10**d)+pi for hi in h for pi in p[-1] if isprime(hi*(10**d)+pi)==1]
    for i in tmp1:
        flg=0
        for j in range(d,0,-1):
            if isprime(i//(10**j))==0:
                flg=1
                break
        if flg==0:
            slst.append(i)
    newp=[mi*(10**d)+pi for mi in m for pi in p[-1] if isprime(mi*(10**d)+pi)==1]
    p.append(newp)
    d+=1
print(sum(slst))
