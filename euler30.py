'''
Project Euler Problem #30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
flst=[]
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        k=i1*100000+i2*10000+i3*1000+i4*100+i5*10+i6
                        if k==i1**5+i2**5+i3**5+i4**5+i5**5+i6**5 and k>9:
                            flst.append(k)
print(sum(flst))
