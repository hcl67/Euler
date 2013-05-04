'''
Project Euler Problem #48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

def dp10(d,p):
    s=1
    for i in range(p):
        s=(s*d)%10000000000
    return s

r=0
for i in range(1,1001):
    r=(r+dp10(i,i))%10000000000
print(r)
        
