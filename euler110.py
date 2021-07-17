'''
euler 110
设 x<=y, 则 n(x+y) = xy => (x-n)y = nx 令 x-n = k => x = n+k; y = nx/k = n + n^2/k; 又 x <= y => k <= n
故 对任意n, 可取 k<=n, k | n^2 则 k 对应一组x,y。
原题<=>求 n^2的<=n小的因子 = (n^2的因字数 + 1) /2

若以 K = [k1,k2,k3,k4,k5] 表示 n 的素因子的幂次，则n 的所有因子数 = (k1+1)(k2+1)(k3+1)(k4+1)(k5+1)
n^2 的所有因子数 = (2*k1+1)(2*k2+1)(2*k3+1)(2*k4+1)(2*k5+1)
易发现因子数与K的顺序无关，则最小化 n <=> K 逆序排列

原题<=>求满足条件的K

遍历：
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  

'''
import datetime,math


shortprime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

btime  = datetime.datetime.now()
def cal110(kl):
    ans = 1
    for i in kl:
        ans *= 2*i + 1
    return ans


  
def gen110(kl):
    n = len(kl)
    if n > len(shortprime):
        return -1
    ans = 1
    for i in range(n):
        ans *= shortprime[i]**kl[i]
    return ans
  
#n = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]    

kl = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

n = len(kl)

thrd = 4000000 * 2
'''
while(cal110(kl)<thrd):
    x = [math.log((2*kl[i]+3)/(2*kl[i]+1))/math.log(shortprime[i]) for i in range(n)]
    ind1 = max(list(range(len(x))),key = lambda i:x[i])
    kl[ind1] += 1
#    print(kl)
#    print([(2*kl[i]+3)/(2*kl[i]+1)/shortprime[i] for i in range(n)])
    x2 = [math.log((2*kl[i]+1)/(2*kl[i]-1))/math.log(shortprime[i]) for i in range(n) if kl[i]>0]
    ind2 = min(list(range(len(x2))),key = lambda i:x2[i])
    if ind2 != ind1:
        kl[ind2] -= 1
#        print(kl)
# 结果再适当缩小，人肉尝试
print(kl,gen110(kl),cal110(kl))    
'''  
#暴力搜索结果
ans = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0] 
bstnum = gen110([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
def find110(kl):
    global ans,bstnum
    if gen110(kl) > bstnum:
        print("failed kl:",kl)
        return
    elif cal110(kl) > thrd:
        ans = kl
        bstnum = gen110(kl)
        print(ans,gen110(ans),cal110(ans))
        return
    else:
        find110([kl[j] + 1 if j == 0 else kl[j] for j in range(len(kl))])
        for i in range(1,len(kl)):
            if kl[i] < kl[i-1]:
                find110([kl[j] + 1 if j == i else kl[j] for j in range(len(kl))])             
                    
find110(ans)    
print()
print(ans,gen110(ans),cal110(ans))    
  
print(datetime.datetime.now() - btime)    
kl = [4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(gen110(kl),cal110(kl),cal110(kl)>4000000*2)
kl2 = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
#print(cal110(kl1)/cal110(kl2),gen110(kl1)/gen110(kl2))
print(gen110(kl2),cal110(kl2),cal110(kl2)>4000000*2)
kl3 = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
#print(cal110(kl1)/cal110(kl2),gen110(kl1)/gen110(kl2))
print(gen110(kl3),cal110(kl3),cal110(kl3)>4000000*2)
