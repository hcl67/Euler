'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import math

l_x=[]
l_xsort=[]
l_count=[]
for i in range(345,10000):
    x = int(math.pow(i,3))
    xsort=''.join(sorted(str(x)))
    #print(x,xsort)
    if xsort not in l_xsort:
        l_x+=[x]
        l_xsort+=[xsort]
        l_count+=[1]
    else:
        n=l_xsort.index(xsort)
        l_count[n]+=1
        if l_count[n]==5:
            print(l_x[n])
            break
    

