'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

import math

n=9
p=2
while(True):
    for k in range(2,10):
        kp=str(int(math.pow(k,p)))
        if len(kp)==p:
            print(kp,k,p)
            n+=1
    if len(kp)<p:
        break
    p+=1
print(n)
    

