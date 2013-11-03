'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''
MAXD=1000000
P_filename="Prime1000000.txt"
P_list=[int(x) for x in open(P_filename,'r').readline().split()]
#print(len(P_list))
    
def UniPfctr(x):
    if x in P_list:
        return [x]
    else:
        r_list=[]
        for p in P_list:
            if p>x:
                break
            elif x%p==0:
                while x%p==0:
                    x/=p
                r_list.append(p)
        return r_list

def CalPhi(x):
    x_plist=UniPfctr(x)
    r=x
    for p in x_plist:
        r=r-r//p
    return r

def CalPhi2(x):
    if x in P_list:
        return x-1
    else:
        for p in P_list:
            if x%p==0:
                break
        x2=x//p
        if (x2)%p==0:
            return CalPhi2(x2)*p
        else:
            return CalPhi2(x2)*(p-1)


#print(CalPhi(1000000))
#print(CalPhi2(1000000))


##if __name__ == '__main__':
##    import timeit
##    print(timeit.timeit("CalPhi2(1000000)", setup="from __main__ import CalPhi2",number=100))
##    print(timeit.timeit("CalPhi(1000000)", setup="from __main__ import CalPhi",number=100))
##    


c=0
for d in range(2,MAXD+1):
    c+=CalPhi(d)
    if d%10000==0:print(d)
print(c)

