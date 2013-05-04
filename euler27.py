'''
Project Euler Problem #27

Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|<1000 and |b|<1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
import math
prime=[2]
x=3
while x<=100000:
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

a=[i for i in range(-999,1000)]
b=[i for i in range(1,1000) if i in prime]
p=[[i,j] for i in a for j in b if 1+i+j in prime]
print(1)
n=2
while len(p)>1:
    p2=[]
    for i in p:
        if n*n+n*i[0]+i[1] in prime:
            p2.append(i)
    n+=1
    p=p2
    print(n,len(p))
    if len(p)<40:
        print(p)
print(n,p,p[0][0]*p[0][1])

