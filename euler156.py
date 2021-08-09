'''
1.考虑计算到整数 10**k (<10**k)，共有k位数字，每位数字平均出现0~9,(算leading0),每个数字出现平均位1/10,所以共出现数字d
10**(k-1)*k次
2.考虑计算到整数 c*10**5 (<10**k)，若c<=d则为 c*10**(k-1)*k，若c>d则为c*10**(k-1)*k+10**k
3.对任意整数，如n = abc = a*10**2 + b*10**1 + c，需要诸如若中间 a == d, 则还需额外增加abc  

通过正问题和逆问题反复，寻找合适的解
'''



def c1562(c,k,d): #判断<c*10**k里出现过多少个d
    r = 10**(k-1)*k*c    
    if c>d:
        r += 10**k
    return r
    

def c156(n,d): #判断<=n里出现过多少个d
    sn = str(n)
    ln = len(sn)
    r = 0
    for k in range(ln-1):
        kd = int(sn[k])
        r += c1562(kd,ln-k-1,d)
        if kd == d:
            r += int(sn[k+1:]) + 1
    kd = int(sn[-1])
    if kd >= d:
        r += 1
    return r

def c156r(n,d): #c156逆问题，给定n个d求最接近的要求的num,f(num-1)<=n, f(num)>n
    k = 0    
    r = 1
    while 1:
        t = c156(r,d)
        if t == n:
            return r,True
        elif t<n:
            k += 1
            r *= 10
        else:
            break
    r //= 10
    for ki in range(k-1,-1,-1):
        dr = 10**ki
        r += dr
        while 1:
            t = c156(r,d)
            if t == n:
                return r,True
            elif t < n:
                r += dr
            else:
                break
        r -= dr
    return r+1,False
        
ans = []
maxk = 1e20
for d in range(1,10):
    print()
    print(d)
    N = 10000
    ansd = [0]
    while 1:
        iter = 0
        k0 = ansd[-1]+1
        while iter<N:
            iter += 1
            k1,f = c156r(k0,d)
            if k1 <= k0 or k0 > maxk:
                break
            else:
                k0 = k1
        if k1 == k0 and f:
            ansd += [k0]
            print(k0)
            continue
        if k0 > maxk:
            break
        iter = 0  
        while iter<N:
            iter += 1
            k1 = c156(k0,d)
            if k1 <= k0 or k0 >maxk:
                break
            else:
                k0 = k1    
        if k1 == k0:
            ansd += [k0]
            print(k0)
            continue
        if k0 > maxk:
            break
    ans += [ansd]    

r = 0
for i in range(len(ans)):
    print(len(ans[i]))
    r += sum(ans[i])
print(r)
