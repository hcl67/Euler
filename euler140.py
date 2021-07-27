#暴力+猜

from math import isqrt,gcd
from datetime import datetime
btime = datetime.now()

'''
phi = (1+sqrt(5))/2
psi = (1-sqrt(5))/2

利用公式 Un = a*phi**n+b*psi**n，有Un = Un-1 + Un-2
U0 = 3
U1 = 1
解：
a = (1-3*psi)/sqrt(5) 
b = (3*phi-1)/sqrt(5) 


AG(x) = sum(Gn*x) = (3-2*x)/(1-x-x*2)-3
AG(x) = k - 3
=>
x = 1/2*k * (2=k+sqrt(5*k**2-16*k+4))
即求k使得 5*k**2-16*k+4 = t**2


'''


ans = [5]
thrd = 30

k = 8
l2 = 5*k**2-16*k+4
while 1:
    k += 1
    l2 +=10*k-21
    l = isqrt(l2)
    if l*l == l2:
        ans += [k]
        k = int(6.8541 * ans[-2])
        l2 = 5*k**2-16*k+4
        
    if len(ans) >= thrd:
        break
    


print(ans[:30])
        
    
print(datetime.now()-btime)
