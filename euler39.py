'''
Project Euler Problem #39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
'''
import math
rtlst=[]
for x in range(3,1001):
    for a in range(1,math.ceil(x/3)):
        for b in range(max(a,x//2-a),math.ceil((x-a)/2)):
            c=x-a-b
            if a**2==(c+b)*(c-b):
                rtlst.append([a,b,c])
slst=[sum(i) for i in rtlst]
n=[0 for i in range(1001)]
for i in slst:
    n[i]+=1
print(n.index(max(n)))
