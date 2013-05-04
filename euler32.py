'''
Project Euler Problem #32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39*186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
slst=[]
p='123456789'

def checkpan(a):
    if int(a[0])*int(a[1:5])==int(a[5:9]) or int(a[0:2])*int(a[2:5])==int(a[5:9]):
        return 1
    else:
        return 0

def permu(a,b):
    if len(b)==0:
        if checkpan(a)==1:
            slst.append(int(a[5:9]))
    else:
        for i in b:
            c=b[:b.index(i)]+b[b.index(i)+1:]
            permu(a+i,c)
    
permu('',p)
print(sum(set(slst)))
                        
