from math import sqrt,gcd
from datetime import datetime
btime = datetime.now()

'''
若素勾股数(a,b,c)满足平铺条件，则(ka,kb,kc)亦满足平铺条件


利用素勾股数公式
a = m**2-n**2
b = 2*m*n
c = m**2+n**2
p = a+b+c = 2*m**2+2*m*n > 2*m**2 + 2*m => n < sqrt(thrd/4)

'''
ans = []
tot = 0
#thrd = 100
thrd = 100000000

MAXM = int(sqrt(thrd/2-1/4)-1/2)+1

for m in range(2,MAXM):
    for n in range(m-1,0,-2):
        if gcd(m,n)>1:
            continue
        a = m**2-n**2
        b = 2*m*n
        c = m**2+n**2 
        p = a + b + c
        if c % abs(b-a)==0:
            ans += [(a,b,c)]
            tot += thrd//p
        
        
    



print(tot)
        
    
print(datetime.now()-btime)
