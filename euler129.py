f = open("d:\Prime10000000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()

def pfdeco(n):
    pf = []
    pn = 0
    p = plist[pn]
    while n>1:
        if n%p == 0:
            pf += [p]
            n //= p
        else:
            pn += 1
            p = plist[pn]
    return pf


from math import gcd



'''
有意思的性质：质数p1,p2,p1!=p2有 p1|R(A(p1)) p2|R(A(p2)) p1*p2|R(A(p1))*p2|R(A(p1))*R(A(p2))|R(A(p1)*A(p2)) R(A(p1)*A(p2))不一定最小
R(LCM(A(p1),A(p2))是最小的

 对于质数p, A(p^n) = A(p)*p^(n-1)

可知p，A(p)<=p，
所以从1000000开始尝试即可

所以 A(p1^m1*p2^m2) = LCM(A(p1)*A(p2))*p1^(m1-1)*p2^(m2-1)


定义B(m,n) = int(('0'*(n-1)+'1')*m)，为p个1，1之间间隔n-1个0的数，则R(n) * B(m,n) = R(m*n) 

因为p|R(A(p)) 所以对任意R(k*A(p)) = B(k,A(p))*R(A(p)) 所以p|R(k*A(p))，又对任意n<A(p)有 p!|R(A(p))所以
R(k*A(p)+n) = R(k*A(p))*10^n+R(n) 不能被p整除，

因为p|R(A(p)),所以 10^A(p)%p = (9*R(A(p))+1)%p = 1, 所以利用A129的方法可知p|B(p,A(p)) ，且是满足条件的最小的B(k,A(p))
 p^2|R(A(p))*B(p,A(P)) = R(p*A(p)), A(p^2) = A(p)*p，同理A(p^n) = A(p)*p^(n-1)

'''

thrd = 1000000

def A129(n):
    if gcd(n,10) > 1:
        return -1
    sumr = 1
    cr = 1
    k = 1
    while sumr % n != 0:
        cr  = cr * 10 % n
        sumr += cr
        k += 1
    return k


# 先看下1000000以上的质数的结果


for p in plist:
    if p < thrd:
        continue
    else:
        pdet = A129(p)
        print(p,pdet)
    if pdet > thrd:
        break

for x in range(1000000,1000171):
    print(x,A129(x))
    

'''
    
pdet = {}
for p in plist:
    if p in {2,5}:
        pdet[p] = -1
    else:
        pdet[p] = A129(p)
    if pdet[p] > thrd:
        break
    
print("prime init done")
        
def A1292(n):
    pf = pfdeco(n)
    pset = set(pf)
    ans = 1
    for p in pset:
        n = pf.count(p)
        ans *= pdet[p]*p**(n-1)
    return ans

det = {}
n = 1

while 1:
    n+=2
    if gcd(n,10) > 1:
        continue
    k = A1292(n)
    if k > thrd:
        break
    det[n] = k

print(n)
        
'''        
    
