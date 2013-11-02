'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''
MAXD=1000000

def HCF(a,b):  ##find the highest common factor of a,b
    x=max(a,b)
    y=min(a,b)
    while x%y!=0:
        t=x%y
        x=y
        y=t
    return y

g_n=0
g_f=0
for d in range(1,MAXD+1):
    n=int(d*3/7)
    if n<1: continue
    if n==d*3/7: continue
    if HCF(n,d)>1: continue
    if n/d>g_f:
        g_n=n
        g_f=n/d
print(g_n)
print(g_f,3/7)
