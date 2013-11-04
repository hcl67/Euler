# -*- coding: utf-8 -*-
'''It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
'''
m>n
m and n are coprime
m − n is odd 

a=k*(m**2-n**2)
b=k*(2*m*n)
c=k*(m**2+n**2)

a+b+c=k*(2*m**2+2*m*n)=2*k*m*(m+n)

m + n is odd
m and m + n are coprime

if T is unique (sided right angle triangle)

< = >

T / 2 = k * p1 * p2

is unique presenting form while 2 * p1 > p2 > p1, p2 is odd, p1 and p2 are coprime


'''

from math import sqrt

def HCF(a,b):  ##find the highest common factor of a,b
    x=max(a,b)
    y=min(a,b)
    while x%y!=0:
        t=x%y
        x=y
        y=t
    return y


MAX=1500000//2
LIMIT=int(sqrt(MAX*2))+1


l_k=[0 for i in range(MAX+1)]

for p1 in range(3,LIMIT):
    if p1%2==0: continue
    for p2 in range(p1//2+1,p1):
        if HCF(p1,p2)>1:
            continue
        p=p1*p2
        k=p
        while 1:
            if k>MAX:
                break
            l_k[k]+=1
            k+=p
    if p1%100==0:
        print(p1)
#print(l_p)
#print(l_k)
count=0
for s in l_k:
    if s==1:
        count+=1
        
print(count)


'''
MAX=50#1500000

l=[]
r=0
for T in range(MAX/2+1):
    c=0
    for k in range(1,T//6+1):
        print(T,k)
        if c>1:
            break
        if T%k>0:
            continue
        for p2 in range(int(sqrt(T//k)+1),int(sqrt(T//k*2))+1):
            print(T,k,p2)
            if p2%2==0:
                continue
            if T//k%p2==0:
                c+=1
    if c==1:
        l+=[T*2]
        print(l)
        r+=1
        
print(l)
print(r)
'''
