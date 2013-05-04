'''
Project Euler Problem #33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
def lgstcommfctr(a,b):
    x=max(a,b)
    y=min(a,b)
    while x%y!=0:
        t=x%y
        x=y
        y=t
    return y

p=[]
dlst=[str(i)+str(j) for i in range(1,10) for j in range(1,10)]
for i in dlst:
    for j in range(1,10):
        if   int(i)/int(i[0]+str(j))==int(i[1])/j and int(i[1])/j<1:
            p.append([int(i),int(i[0]+str(j))])
        elif int(i)/int(i[1]+str(j))==int(i[0])/j and int(i[0])/j<1:
            p.append([int(i),int(i[1]+str(j))])
        elif int(i)/int(str(j)+i[0])==int(i[1])/j and int(i[1])/j<1:
            p.append([int(i),int(str(j)+i[0])])
        elif int(i)/int(str(j)+i[1])==int(i[0])/j and int(i[0])/j<1:
            p.append([int(i),int(str(j)+i[1])])
n=1
d=1
for i in p:
    n*=i[0]
    d*=i[1]
k=lgstcommfctr(n,d)
print(d//k)
                    
