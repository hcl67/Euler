'''
Project Euler Problem #10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import math
prime=[2]
sump=2
x=3
while x<=2000000:
    flg=0
    sqx=int(math.sqrt(x))
    for d in prime:
        if x%d==0:
            flg=1
            break
        if d>sqx:
            break
    if flg==0:
        sump+=x
        prime.append(x)
    x+=2
print(sump)

