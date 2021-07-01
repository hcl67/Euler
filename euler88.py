import math,datetime,sys

MAXN = 12000

'''
注意到：
k: n = f(k) 对有性质： pdt(ai,1~n)-sum(ai-1,1~n) : pdt(ai,1~n) 
ai >= 2

令 t = -sum(ai-1,1~n), 则 f(n-t) = n

易得 对任意 k,f(k)<=2k 即对任意n, f~(n) >= n/2
 
'''

original_stdout = sys.stdout 

def genpart(n,k):
    if n==0:
        return [[]]
    elif n<k:
        return [[-1]]
    elif n//k < 2:
        return [[n]]
    lf = []
    for i in range(k,n+1):
        li = genpart(n-i,i)
        for t in li:
            if -1 in t:
                continue
            lf.append([i]+t)
    return lf


#print(genpart(9,1))


def genfac(n,k):
    if n == 1:
        return[[]]
    elif n<k:
        return [[-1]]
    elif n==k:
        return [[k]]
    lf = []
    for i in range(k, n+1):
        if n//i*i==n:
            li = genfac(n//i,i)
            for t in li:
                if -1 in t:
                    continue
                lf.append([i]+t)
    return lf



#print(genfac(32,2))

btime = datetime.datetime.now()

MAXN = 24000

ans = [-1] * (MAXN+1)
for t in range(MAXN,1,-1):
    lf = genfac(t,2)
#    setf = set()
    for f in lf[:-1]:
#        setf = set.union(setf, set(f))
        n = t
        k = n - sum(f) + len(f)
        ans[k] = t
#    print(t,":",len(setf))
print(ans[2:(MAXN//2+1)])
print(sum(set(ans[2:(MAXN//2+1)])))    

print(datetime.datetime.now()-btime)      

'''
some test 1

with open('88.txt', 'w') as f:
    sys.stdout = f 

    ans = {}
    for t in range(2,16):
        lp = genpart(t,1)
        print("\nt =",t)
        for p in lp[:-1]:
            a = [1+i for i in p]
            n = math.prod(a)
            k = n - sum(p)
            if k in ans:
                if n not in ans[k]:
                    ans[k].append(n)
            else:
                ans[k] = [n]
            print("k : n = ",k,":",n," via ",a)
    
    print("\nminN")
    for k in sorted(ans):
        print(k, sorted(ans[k]))
        
    sys.stdout = original_stdout 
    
    
'''
