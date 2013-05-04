'''
Project Euler Problem #49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

d4lst=[]
for i1 in range(10):
    for i2 in range(10):
        if i2==i1: continue
        for i3 in range(10):
            if i3==i1 or i3==i2: continue
            for i4 in range(10):
                if i4==i1 or i4==i2 or i4==i3: continue
                d4=[str(i1),str(i2),str(i3),str(i4)]
                d4.sort()
                d4str=d4[0]+d4[1]+d4[2]+d4[3]
                d4lst.append(d4str)
d4set=list(set(d4lst))

d4prime=[]
for i in range(1001,10000,2):
    if isPrime(i) and len(set(str(i)))==4:
        d4prime.append(i)


d4pgrp=[[] for i in d4set]
for i in d4prime:
    d4p=[str(i)[0],str(i)[1],str(i)[2],str(i)[3]]
    d4p.sort()
    d4pstr=d4p[0]+d4p[1]+d4p[2]+d4p[3]
    d4pgrp[d4set.index(d4pstr)].append(i)

d4pgrp2=[i for i in d4pgrp if len(i)>=3]

for i in d4pgrp2:
    for j in range(len(i)-2):
        for k in range(j+1,len(i)-1):
            if i[k]+i[k]-i[j] in i:
                print(i[j],i[k],i[k]+i[k]-i[j])
                

d4lst=[]
for i1 in range(10):
    for i2 in range(10):
        if i2==i1: continue
        for i3 in range(10):
            if i3==i1 or i3==i2: continue
            for i4 in range(10):
                if i4==i1 or i4==i2 or i4==i3: 
                    d4=[str(i1),str(i2),str(i3),str(i4)]
                    d4.sort()
                    d4str=d4[0]+d4[1]+d4[2]+d4[3]
                    d4lst.append(d4str)
d4set=list(set(d4lst))

d4prime=[]
for i in range(1001,10000,2):
    if isPrime(i) and len(set(str(i)))==3:
        d4prime.append(i)


d4pgrp=[[] for i in d4set]
for i in d4prime:
    d4p=[str(i)[0],str(i)[1],str(i)[2],str(i)[3]]
    d4p.sort()
    d4pstr=d4p[0]+d4p[1]+d4p[2]+d4p[3]
    d4pgrp[d4set.index(d4pstr)].append(i)

d4pgrp2=[i for i in d4pgrp if len(i)>=3]

for i in d4pgrp2:
    for j in range(len(i)-2):
        for k in range(j+1,len(i)-1):
            if i[k]+i[k]-i[j] in i:
                print(i[j],i[k],i[k]+i[k]-i[j])

