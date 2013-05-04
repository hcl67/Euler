'''
Project Euler Problem #12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
def defactor(x):
    if x==1:
        return [1]
    else: 
        p=[]
        while 1:
            y=int(math.sqrt(x))
            if len(p)==0:
                s=2
            else:
                s=p[-1]
            if s>y:
                p.append(x)
                break
            for i in range(s,y+2):
                  if x%i==0:
                      p.append(i)
                      x=x//i
                      break
            if i>=y:
                p.append(x)
                break
        return p


def countfactor(x):
    p=defactor(x)
    s=1
    if len(p)==1 and p[0]==1:
        return s
    else:
        k=2
        for i in range(1,len(p)):
            if p[i]!=p[i-1]:
                s*=k
                k=2
            else:
                k+=1
        s*=k
        return s


a=1
s=1
k=1
while 1:
    if k>500:
        break
    a+=1
    s+=a
    k=countfactor(s)
print(s,k)

