'''
Project Euler Problem #24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
import math

x=1000000

s=0
p=''
k=[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    for j in range(10-i):
        if s+math.factorial(9-i)<x:
            s+=math.factorial(9-i)
        else:
            p=p+str(k[j])
            del(k[j])
            break
print(p)
