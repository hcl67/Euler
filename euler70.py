'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

mod9

k/1=>k
k/2=>k*(10)/2=>k*5
k/4=>k*(28)/4=>k*7
k/5=>k*2
k/7=>k*4
k/8=>k*8=9-k



p-1/p=0,5,3,8,6,2
    p=1,2,4,5,7,8

=>(2,8)  (5,5)
'''

MAX=10000000
P_filename="Prime10000000.txt"
P_list=[int(x) for x in open(P_filename,'r').readline().split()]

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


#Pm9_list=[x%9 for x in P_list]
P_list_m2=[x for x in P_list if x%9==2]
P_list_m5=[x for x in P_list if x%9==5]
P_list_m8=[x for x in P_list if x%9==8]

maxx=0
minphi=100
for a in P_list_m2:
    for b in P_list_m8:
        if a*b>MAX:
            break
        if a*b/((a-1)*(b-1))<minphi and sorted(str(a*b))==sorted(str((a-1)*(b-1))):
            maxx=a*b
            minphi=a*b/((a-1)*(b-1))

for a in P_list_m5:
    for b in P_list_m5:
        if a*b>MAX:
            break
        if a==b:
            continue
        if a*b/((a-1)*(b-1))<minphi and sorted(str(a*b))==sorted(str((a-1)*(b-1))):
            maxx=a*b
            minphi=a*b/((a-1)*(b-1))
        
print(maxx)
            
            
