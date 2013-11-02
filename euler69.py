# -*- coding: cp936 -*-
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
MAX=1000000
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

##def CalPhi2(x):
##    x_plist=UniPfctr(x)
##    full_unprime_set=set([i+1 for i in range(x)])
##    for p in x_plist:
##        n=x//p
##        full_unprime_set-=set([(i+1)*p for i in range(n)])
##    return len(full_unprime_set)

def CalPhi(x):
    x_plist=UniPfctr(x)
    r=x
    for p in x_plist:
        r*=(1-1/p)
    return r


##if __name__ == '__main__':
##    import timeit
##    print(timeit.timeit("CalPhi2(1000000)", setup="from __main__ import CalPhi2",number=10))
##    print(timeit.timeit("CalPhi(1000000)", setup="from __main__ import CalPhi",number=10))
    

  
##maxn=0
##maxn2phi=0
##for n in range(2,MAX+1):
##    if n/CalPhi(n)>maxn2phi:
##        maxn,maxn2phi=n,n/CalPhi(n)
##    if float(n)*1000/MAX==int(float(n)*1000/MAX):
##        print(n)
##
##print(maxn)

x=1
for i in P_list:
    if x*i>MAX:
        break
    x*=i

print(x)
    

