﻿'''
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	        	P4,n=n2	        	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''

import math


def Triangle(n):
    return n*(n+1)/2

def calTriangle(x):
    return (math.sqrt(1+8*x)-1)/2

def isTriangle(x):
    n = calTriangle(x)
    return n==int(n)

def Square(n):
    return n*n

def calSquare(x):
    return math.sqrt(x)

def isSquare(x):
    n = calSquare(x)
    return n==int(n)

def Pentagonal(n):
    return n*(3*n-1)/2

def calPentagonal(x):
    return (math.sqrt(1+24*x)+1)/6

def isPentagonal(x):
    n = calPentagonal(x)
    return n==int(n)

def Hexagonal(n):
    return n*(2*n-1)

def calHexagonal(x):
    return (math.sqrt(1+8*x)+1)/4

def isHexagonal(x):
    n = calHexagonal(x)
    return n==int(n)

def Heptagonal(n):
    return n*(5*n-3)/2

def calHeptagonal(x):
    return (math.sqrt(9+40*x)+3)/10

def isHeptagonal(x):
    n = calHeptagonal(x)
    return n==int(n)

def Octagonal(n):
    return n*(3*n-2)

def calOctagonal(x):
    return (math.sqrt(4+12*x)+2)/6

def isOctagonal(x):
    n = calOctagonal(x)
    return n==int(n)

def Permutate(l):
    if len(l)==1:
        return [l]
    else:
        returnlist=[]
        for i in range(len(l)):
            t=[x for x in l]
            t.pop(i)
            p=Permutate(t)
            for j in p:
                returnlist+=[[l[i]]+j]
        return returnlist



Triangle_list=[Triangle(n) for n in range(int(calTriangle(1000))+1,int(calTriangle(9999)+1))]
Square_list=[Square(n) for n in range(int(calSquare(1000))+1,int(calSquare(9999)+1))]
Pentagonal_list=[Pentagonal(n) for n in range(int(calPentagonal(1000))+1,int(calPentagonal(9999)+1))]
Hexagonal_list=[Hexagonal(n) for n in range(int(calHexagonal(1000))+1,int(calHexagonal(9999)+1))]
Heptagonal_list=[Heptagonal(n) for n in range(int(calHeptagonal(1000))+1,int(calHeptagonal(9999)+1))]
Octagonal_list=[Octagonal(n) for n in range(int(calOctagonal(1000))+1,int(calOctagonal(9999)+1))]
All_list=[Triangle_list,Square_list,Pentagonal_list,Hexagonal_list,Heptagonal_list,Octagonal_list]


#print(Octagonal_list[0],Octagonal_list[-1])
#print(calOctagonal(65))

breaktag=0

fullp=Permutate([0,1,2,3,4,5])
for li in fullp:
    if breaktag==1:
        break
    #print(li)
    l1=All_list[li[0]]
    l2=All_list[li[1]]
    l3=All_list[li[2]]
    l4=All_list[li[3]]
    l5=All_list[li[4]]
    l6=All_list[li[5]]
    for i1 in l1:
        if breaktag==1:
            break
        #print(i1)
        h1=i1%100
        for i2 in l2:
            if breaktag==1:
                break
            if int(i2/100)!=h1:
                continue
            else:
                #print(i1,i2)
                h2=i2%100
                for i3 in l3:
                    if breaktag==1:
                        break
                    if int(i3/100)!=h2:
                        continue
                    else:
                        #print(i1,i2,i3)
                        h3=i3%100
                        for i4 in l4:
                            if breaktag==1:
                                break
                            if int(i4/100)!=h3:
                                continue
                            else:
                                #print(i1,i2,i3,i4)
                                h4=i4%100
                                for i5 in l5:
                                    if breaktag==1:
                                        break
                                    if int(i5/100)!=h4:
                                        continue
                                    else:
                                        #print(i1,i2,i3,i4,i5)
                                        h5=i5%100
                                        for i6 in l6:
                                            if breaktag==1:
                                                break
                                            if int(i6/100)!=h5:
                                                continue
                                            else:
                                                #print(i1,i2,i3,i4,i5,i6)
                                                h6=i6%100
                                                if int(i1/100)!=h6:
                                                    continue
                                                else:
                                                    print(i1,i2,i3,i4,i5,i6)
                                                    print(i1+i2+i3+i4+i5+i6)
                                                    print(li)
                                                    breaktag=1
                                                                
    
    
