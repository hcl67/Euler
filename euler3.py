'''
Project Euler Problem #3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
print(defactor(600851475143))

