'''
euler 108
设 x<=y, 则 n(x+y) = xy => (x-n)y = nx 令 x-n = k => x = n+k; y = nx/k = n + n^2/k; 又 x <= y => k <= n
故 对任意n, 可取 k<=n, k | n^2 则 k 对应一组x,y。
原题<=>求 n^2的<=n小的因子 = (n^2的因字数 + 1) /2

若以 K = [k1,k2,k3,k4,k5] 表示 n 的素因子的幂次，则n 的所有因子数 = (k1+1)(k2+1)(k3+1)(k4+1)(k5+1)
n^2 的所有因子数 = (2*k1+1)(2*k2+1)(2*k3+1)(2*k4+1)(2*k5+1)
易发现因子数与K的顺序无关，则最小化 n <=> K 逆序排列

原题<=>求满足条件的K

遍历：
[1,1,1,1,1,1,1]
[2,2,1,1,1,1]  <------
[4,1,1,1,1,1]
[2,2,2,2,2]
[3,2,2,2,1]
[3,3,2,1,1]
[4,2,2,1,1]
[12,1,1,1,1]
[4,3,3,2]

'''
import datetime


shortprime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

btime  = datetime.datetime.now()
def cal108(n):
    ans = 0
    n2 = n**2
    for i in range(1,n+1):
        if n2 % i == 0:
            ans += 1
    return ans


  
def gen108(kl):
    n = len(kl)
    if n > len(shortprime):
        return -1
    ans = 1
    for i in range(n):
        ans *= shortprime[i]**kl[i]
    return ans
  
n = gen108([4,3,3,2])    
    
print(n, cal108(n))  
    
  
print(datetime.datetime.now() - btime)    
