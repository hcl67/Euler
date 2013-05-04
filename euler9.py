'''
Project Euler Problem #9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 2**5 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find():
    for a in range(1,334):
        for b in range(max(a,500-a),(1000-a)//2):
            c=1000-a-b
            if a**2==(c+b)*(c-b):
                print(a,b,c)
                print(a*b*c)
                return
find()
