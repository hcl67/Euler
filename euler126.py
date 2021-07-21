
def cal1262(elt,n):
 

    lylt = [elt[0]*elt[1]]
    for i in range(1,n+1):
        lylt += [2*(elt[0]+elt[1])+4*(i-1)]
    return lylt[n]*elt[2]+sum(lylt[:n])*2

'''
经计算化简有给定a,b,c,n，f(a,b,c,n)的逻辑：
2(ab+ac+bc)+4(n-1)(a+b+c+n-2)

df/da = 2(b+c)+4(n-1)
df/dn = 4(a+b+c+2*n-2)

'''

def cal126(a,b,c,n):   
    return 2*(a*b+a*c+b*c)+4*(n-1)*(a+b+c+n-2)


    
from collections import defaultdict
import queue



cap = 20000
dq = queue.Queue()
dq.put((1,1,1,1,6))
df = defaultdict(list)
df[6] += [(1,1,1,1)]
dset = {(1,1,1,1)}
while not dq.empty():
    a,b,c,n,s = dq.get()
    if (a+1,b,c,n) not in dset:
        sa = s+2*(b+c)+4*(n-1)
        if sa < cap:
            dset.add((a+1,b,c,n))
            dq.put((a+1,b,c,n,sa))
            df[sa] += [(a+1,b,c,n)]
    if (a,b+1,c,n) not in dset and b < a:
        sb = s+2*(a+c)+4*(n-1)
        if sb < cap:
            dset.add((a,b+1,c,n))
            dq.put((a,b+1,c,n,sb))
            df[sb] += [(a,b+1,c,n)]
    if (a,b,c+1,n) not in dset and c < b:
        sc = s+2*(a+b)+4*(n-1)
        if sc < cap:
            dset.add((a,b,c+1,n))
            dq.put((a,b,c+1,n,sc))
            df[sc] += [(a,b,c+1,n)]
    if (a,b,c,n+1) not in dset:
        sn = s+4*(a+b+c+n+n-2)
        if sn < cap:
            dset.add((a,b,c,n+1))
            dq.put((a,b,c,n+1,sn))
            df[sn] += [(a,b,c,n+1)]
                
lf = list(sorted(df.keys(), key = lambda x:-len(df[x])))
print(lf[0],len(df[lf[0]]))
               
print(sorted(list(dict(filter(lambda x:len(x[1])==1000,df.items())).keys()))[0])
