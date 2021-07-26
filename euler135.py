from datetime import datetime

btime = datetime.now()


__f = open("d:\prime1000000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split(" ")))
__f.close()

def pfdeco(n):
    from collections import defaultdict
    pf = defaultdict(int)
    pn = 0
    p = __plist[pn]
    while n>1:
        if n%p == 0:
            pf[p] += 1
            n //= p
        elif p*p > n:
            pf[n] += 1
            break
        else:
            pn += 1
            p = __plist[pn]
    return pf

def fct(n):
    pfdict = pfdeco(n)
    fct = [1]
    for k,v in pfdict.items():
        kv = [k**i for i in range(v+1)]
        fct = [x*y for x in fct for y in kv]
    return sorted(fct)




thrd = 1000000
ans = []
tgt = 10


# 调整一下，只需遍历一半就行了

for n in range(1,thrd):
    fctlist = fct(n)  
    k = 0
    lenfct = len(fctlist) 
    for i in range(lenfct-1,lenfct//2-1,-1):
        y = fctlist[i]
        x = fctlist[lenfct-1-i]
        ss = sqrt(n/3)
        if (x + y) % 4 == 0:
            if x <= ss or x==y:
                k+=1
            else:
                k+=2
    if k == 1:
        ans += [n]




# for n in range(1000,thrd):
#     fctlist = fct(n)  
#     if len(fctlist) < tgt:
#         continue
#     k = 0
#     for y in fctlist:
#         if (n//y + y) % 4 == 0 and (n//y + y) // 4 < y:
#             k += 1
#     print(n,fctlist,k)
#     if k == tgt:
#         ans += [n]        
        
print(len(ans))

print(datetime.now()-btime)
