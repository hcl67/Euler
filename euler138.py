from math import isqrt
from datetime import datetime
btime = datetime.now()

'''
(b/2)^2+h^2=L^2
h = b+/-1
1)令
b/2 = 2mn
h = m^2-m^2 
则化简有
m = 2n+sqrt(5n^2+/-1)

5*n^2 = t^2+/-1  

1)令
b/2 = m^2-m^2 
h = 2mn
则化简有
m = 1/2(n+sqrt(5n^2+/-2)) 无解
'''
i = -1
ans = []
tgt = 12
while 1:
    i += 1
    for j in [1,2,3,4,6,7,8,9]:
        t=10*i+j
        if j in [1,4,6,9]:
            n2 = (t**2-1)//5
        else:
            n2 = (t**2+1)//5
        if n2 <= 0:
            continue
        n = isqrt(n2)
        if n**2 == n2:
            m = 2*n+t
            ans += [(4*m*n,m**2-n**2,m**2+n**2,t,m,n)]
    if len(ans) == tgt:
        break

print(sum(map(lambda x:x[2],ans)))
        
    
print(datetime.now()-btime)
