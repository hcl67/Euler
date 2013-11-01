# -*- coding: cp936 -*-
'''
All square roots are periodic when written as continued fractions and can be written in the form:

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''
from math import sqrt

def conFrac(n):
    a1=int(sqrt(n))
    a2=a1
    a3=1
    seq=[[a1,a2,a3]]
    while(True):
        #print(seq)
        b1=a1
        b2=a2
        b3=a3
        a1=int(b3/(sqrt(n)-b2))
        a3=(n-b2*b2)/b3
        a2=a1*a3-b2
        if [a1,a2,a3] not in seq:
            seq+=[[a1,a2,a3]]
        else:
            p=seq.index([a1,a2,a3])
            return len(seq)-p

n=0
for i in range(1,10000):
    if sqrt(i)==int(sqrt(i)):
        continue
    if conFrac(i)%2==1:
        n+=1
print(n)
    

    
    
