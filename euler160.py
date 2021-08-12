timestamp = []

def timemark(printflag = False):
    from datetime import datetime
    global timestamp
    ts = datetime.now()
    if len(timestamp) == 0:
        timestamp = [ts]
    else:    
        timestamp[-1] = ts - timestamp[-1]
        timestamp += [ts]
    if printflag:
        for i in range(len(timestamp)-1):
            print(timestamp[i])
        timestamp = []
    return 
        


def pnp(n,p):  #<=n的数中，含质数p的总量，即P(N)中p的幂次
    if p == 1:
        return n
    r = 0
    pp = p
    while pp <= n:
        r += n//pp
        pp *= p
    return r


timemark()


'''
跳过5的倍数后的阶乘的尾数不变，但需注意要留出足够的2与5组成10，考虑所有100000!，并且对其中所有的偶数留出一个2，足够使用。
最后将多出的2乘回去

9376
40000
'''

def c160(n, d): #计算跳过所有5的倍数及所有偶数/2后的尾数
    if n > d:
        kd = n//d
        kr = n%d 
        rnum, rcnt2 = c160(kr,d)
        dnum, dcnt2 = c160(d,d)
        num = 1
        for i in range(kd):
            num *= dnum
            num %= d
        num *= rnum
        num %= d
        cnt2 = dcnt2*kd+rcnt2
    else:
        num = 1
        cnt2 = 0
        for i in range(2,n+1):
            if i%5==0:
                continue
            elif i%2 == 0:
                num *= i//2
                cnt2 += 1
            else:
                num *= i
            num %= d        
    return num,cnt2


def pnd(p,n,d):  #计算p的n次方mod d
    l = []
    while n>0:
        l+=[n%2]
        n //=2
    num = 1
    for i in range(len(l)-1,-1,-1):
        num *= p**l[i] * num
        num %= d
    return num
        



N = 1000000000000
d = 100000

dnum,dcnt2 = c160(d,d)
k = N
num,cnt2,cnt5 = 1,0,0
while k>0:
    kd = k//d
    kr = k%d
    rnum, rcnt2 = c160(kr,d)
    for i in range(kd):
        num *= dnum
        num %= d
    num *= rnum
    num %= d
    cnt2 += dcnt2*kd+rcnt2
    cnt2 -= cnt5
    k //= 5
    cnt5 = k

num *= pnd(2,cnt2,d)
num %= d
print(num)


'''
#N = 1000000000000
N = 100000000


ans = 1
cnt = 0

for i in range(2,N+1):
    k = i
    while k%5 == 0:
        cnt += 1
        k //= 5
    while cnt > 0 and k%2 == 0:
        k //= 2
        cnt -= 1
    ans *= k
    ans %= 100000
    
print(ans)

timemark()  

#最大到5^18次方,即要保证尾数正确，至少要保留18位非零数字

K = 10**18

ans = 1

for i in range(2,N+1):
    ans *= i
    while ans % 10 ==0:
        ans //= 10
    ans %= K
    
print(ans%100000)
  
'''
  
timemark(True)    



