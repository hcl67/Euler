'''
费马点
p,q,r
a**2 = p**2+q**2+p*q
b**2 = p**2+r**2+p*r
c**2 = r**2+q**2+r*q


当a=b时 a**2+b**2+ab = 3a**2 不可能是完全平方数
当 a|b时 a**2+b**2+ab = a**2(p**2+p+1) 不可能是完全平方数


生成可能的p,q对，然后在里面找p,q,r

p**2+q**2+p*q = a**2 配方后有
(4p+2q)^2+12q^2 = (4a)^2

令 
4p+2q = m^2-3n^2 => p = 1/4(m+n)(m-3n)
q = mn
4a = m^2+3n^2

m,n必须同奇时，gcd(m,n)=1,同偶时，gcd(m,n)=2, (m+n) % 4 =2，即m/2,n/2不同奇偶，且gcd(m/2,n/2)=1
m>n，m%3>0




所以有 n < min(m,thrd//m), n >  max(1,1/3(m-sqrt(thrd)))


换一组生成公式对照：
p = m^2-n^2
q = 2mn+n^2
a = m^2+n^2+mn
m-n % 3 > 0  m>n gcd(m,n) = 1


'''
from math import isqrt,gcd
from datetime import datetime
from collections import defaultdict
btime = datetime.now()


def edgecheck143(p,q):
    a2 = p**2+q**2+p*q
    if isqrt(a2)**2==a2:
        return isqrt(a2)
    else:
        return -1

def edgecheck1432(p,q,r):
    return edgecheck143(p,q),edgecheck143(p,r),edgecheck143(q,r)
# thrd = 120000

thrd = 120000

dict143p = defaultdict(set)
for m in range(2,thrd):
#    for n in range(1,m):
    for n in range(max(1,(m-isqrt(4*thrd))//3),min((m+1)//3,thrd//m+1)*3):
#        if (m%2==1 and n%2==1) or (m%2==0 and n%2==0): 
        if (m%2==1 and n%2==1 and gcd(m,n)==1 and m%3>0) or (m%2==0 and n%2==0 and (m+n)%4==2 and gcd(m,n)==2 and m%3>0): 

            q = m*n
            p = (m**2-3*n**2-2*q)//4
            if p<q:
                p,q = q,p
            if p+q<thrd and q>0:
                dict143p[p].add(q)

            # q = m*n    
            # p = (m**2*3-n**2-2*q)//4
            # if p<q:
            #     p,q = q,p
            # if p+q<thrd and q>0 and edgecheck143(p,q)>0:
            #     dict143p[p].add(q)  



# dict143p2 = dict143p            

      
# dict143p = defaultdict(set)
# for m in range(2,isqrt(thrd)+1):
# #    for n in range(1,m):
#     for n in range(1,min(m,isqrt(thrd//3)+1)):
# #        if (m%2==1 and n%2==1) or (m%2==0 and n%2==0): 
#         if gcd(m,n)==1 and (m-n)%3 > 0 : 

#             q = 2*m*n+n**2
#             p = m**2-n**2
#             if p<q:
#                 p,q = q,p
#             if p+q<thrd:
#                 dict143p[p].add(q)

# for k,v in dict143p.items():
#     if k not in dict143p2:
#         print(k,v)
#         break

dict143 = defaultdict(set)
for k,vs in dict143p.items():
    n = thrd//k
    for i in range(1,n+1):
        dict143[k*i].update(set([x * i for x in vs]))


ans = defaultdict(list)


for p,qs in dict143.items():
    if len(qs) < 2:
        continue
    for q in qs:
        if q not in dict143:
            continue
        rs = dict143[q].intersection(qs)
        if len(rs) < 1:
            continue
        for r in rs:
            d = p+q+r
            if d <= thrd:
                ans[d] += [(p,q,r)]

check = []
for k,ds in ans.items():
    for d in ds:
        check += [(edgecheck1432(d[0],d[1],d[2]))]
        
for tri in check:
    if tri[0]**2 >= tri[1]**2+tri[2]**2+tri[1]*tri[2]:
        print(tri)

           


print(sum(ans.keys())) 
print(len(ans))
print(sum([len(v) for k,v in ans.items()]))     





def check143(n):
#    for r in range(1,n//3):
#        for q in range(r+1,(n-r)//2):
    for r in range(1,n-2):
        for q in range(1,n-r):


            p = n-q-r
            # if gcd(gcd(p,q),r)>1:
            #     continue
            # if p%r == 0 or p%q == 0 or q%r == 0:
            #     continue
            a2 = p**2+q**2+p*q
            b2 = p**2+r**2+p*r
            c2 = r**2+q**2+r*q
            if isqrt(a2)**2 == a2 and isqrt(b2)**2 == b2 and isqrt(c2)**2 == c2:
                print (p,q,r,isqrt(a2),isqrt(b2),isqrt(c2))
                return True,p,q,r
    return False,0,0,0

ans2 = defaultdict(list)


# for n in range(6,thrd+1):
#     flag,p,q,r = check143(n)
#     if flag:
#         ans2[n] += [(p,q,r)]
# print(sum(ans2.keys()))      
    


print(datetime.now()-btime)
            
            
