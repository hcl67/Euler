
  
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
129：
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
 
 
130： 
对于合数 ，由上面的性质可知，若A(k)|(k-1) 则必然 k不能的质因数次数必须=1，(p不可能整除p^n-1)。
同时p不能都是A(p) = p-1,(p1-1)*(p2-1)不能整除p1*p2-1
同时不能是3的倍数，A(3)=3 不整除 3k-1
 
'''

thrd = 20000

def A130(n):
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

pdet = {}
for p in plist:
    pdet[p] = A130(p)
    if p > thrd:
        break


clist = []
n = 5
while len(clist) < 25:
    n+=2
    if n > thrd:
        break
    if gcd(n,30) > 1:
        continue
    pfn = pfdeco(n)
    if len(pfn) == 1 or len(pfn) > len(set(pfn)) or len(pfn) == sum(p == pdet[p] + 1 for p in pfn):
        continue
    else:
        if (n-1) % A130(n) == 0:
            print(n)
            clist += [n]
        
    

    
