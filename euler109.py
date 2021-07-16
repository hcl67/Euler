from itertools import combinations

darts = {}
dartd = {}
dartt = {}
dartb = {'SBull':25,'DBull':50}
for i in range(1,21):
    darts['S'+str(i)] = i
    darts['D'+str(i)] = i * 2
    darts['T'+str(i)] = i * 3
    
dartpool = {}
dartpool.update(darts)
dartpool.update(dartd)
dartpool.update(dartt)
dartpool.update(dartb)

thrd = 100

ans = 0
for tp in combinations(dartpool.keys(),2):
    dartsum = dartpool[tp[0]] + dartpool[tp[1]]
    ans += min(max((thrd - 1 - dartsum)//2,0), 20)
    if dartsum + 50 < thrd:
        ans += 1
    
for tp in dartpool.keys():
    ans += min(max((thrd - 1 - dartpool[tp])//2,0), 20)
    if dartpool[tp] + 50 < thrd:
        ans += 1
    ans += min(max((thrd - 1 - dartpool[tp]*2)//2,0), 20)
    if dartpool[tp]*2 + 50 < thrd:
        ans += 1
    
    
    
ans += min((thrd - 1)//2, 20)
if 50 < thrd:
    ans += 1
    
print(ans)


    
