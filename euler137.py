from math import isqrt
from datetime import datetime
btime = datetime.now()

'''
求解有AF(x) = x/(1-x-x^2)
当AF(x) = k 有 x = (sqrt(5k^2+2k+1)-k-1)/2k 
若x是有理数，则 5k^2+2k+1是完全平方数 
即 (k+1)^2+(2k)^2=s^2
利用勾股数构造公式，
1)令
k+1 = m^2-n^2
2k = 2mn
s = m^2+n^2 
则化简有
m = (n+sqrt(5n^2+4))/2
即求奇数n，使得5n^2+4是完全平方数
5*n^2 = (t+2)(t-2) t是奇数，t 3/7结尾;t是偶数，t 2/8结尾 
m = (n+t)/2

2)令
k+1=2mn
2k=m^2-n^2
则化简有
m = 2n+sqrt(5n^2-2) 无正整数解
'''
i = -1
ans = []
tgt = 15
while 1:
    i += 1
    for j in [2,3,7,8]:
        t=10*i+j
        n2 = (t+2)*(t-2)//5
        if n2 <= 0:
            continue
        n = isqrt(n2)
        if n**2 == n2:
            m = (n+t)//2
            ans += [m*n]
    if len(ans) == tgt:
        break

print(ans)
        
    
print(datetime.now()-btime)
