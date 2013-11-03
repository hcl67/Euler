'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''
T=100
MIND=1
MAXD=12000
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

def multi_list(l):
    k=1
    for i in l:
        k*=i
    return k

def Combination(l,n):  ##genenrate all combination of list l with length n
    if n>len(l) or n<0:
        #print("ERROR n")
        return []
    elif n==1:
        return [[x] for x in l]
    elif n==len(l):
        return [l]
    else:
        rl=[]
        for x in l: 
            xl=Combination(l[l.index(x)+1:],n-1)
            xln=[]
            for y in xl:
                if len(xl)>0:
                    rl.append([x]+y)
        return rl

def CalPhi2(x,n):
    x_plist=UniPfctr(x)
    full_combine=[]
    for i in range(len(x_plist)):
        full_combine+=Combination(x_plist,i+1)
    #print(full_combine)
    factor_list=[]
    sign_list=[]
    for l in full_combine:
        factor_list+=[multi_list(l)]
        sign_list+=[(-1)**(len(l))]
    #print(factor_list)
    #print(sign_list)
    if n<0:
        print("error on n<0: n =",n)
    r=n
    for i in range(len(factor_list)):
        r+=(n//factor_list[i]*sign_list[i])
    return r



c2=0
c3=0
for d in range(MIND,MAXD+1):
    c2+=CalPhi2(d,(d-1)//2)
    c3+=CalPhi2(d,(d-1)//3)
    if d%1000==0:print(d)
print("c2=",c2)
print("c3=",c3)
print(c2-c3-1)


