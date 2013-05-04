'''
Project Euler Problem #5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def countdiv(x,d):
    if d<2:
        return -1
    n=0;
    while x%d==0:
        n=n+1
        x=x//d
    return n

y=19*17*13*11*7*5*9*16
print(y)
d=[]
for i in range(1,21):
    d.append(countdiv(y,i))
print(d)
