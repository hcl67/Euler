'''
Project Euler Problem #35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
import math
prime=[2]
x=3
while x<=1000000:
    flg=0
    sqx=int(math.sqrt(x))
    for d in prime:
        if x%d==0:
            flg=1
            break
        if d>sqx:
            break
    if flg==0:
        prime.append(x)
    x+=2

rp=[]
for i in prime:
    flg=0
    for j in range(1,len(str(i))):
        if int(str(i)[j:]+str(i)[:j]) not in prime:
            flg=1
            break
    if flg==0:
        rp.append(i)
print(len(rp))
