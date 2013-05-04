'''
Project Euler Problem #7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math
prime=[2]
x=3
while len(prime)<=10000:
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
print(prime[-1])        
