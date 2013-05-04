'''
Project Euler Problem #34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math
fact=[math.factorial(i) for i in range(10)]
slst=[]
for i in range(3,10000000):
    s=str(i)
    n=0
    for j in s:
        n+=fact[int(j)]
    if i==n:
        slst.append(i)
        print(i)
print(sum(slst))
