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
        



__f = open("D:\prime1000000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split()))
__f.close()
__pset = set(__plist)

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

def mod9(n):
    return (n-1)%9 +1

def mdrs(n):
    from collections import defaultdict
    pfd = pfdeco(n)
    md = defaultdict(int)
    for k,v in pfd.items():
        md[mod9(k)] +=v
    min24 = min(md[2],md[4])
    md[2] -= min24
    md[4] -= min24
    md[8] += min24
    d3 = md[3]//2
    md[9] += d3
    md[3] -= 2*d3
    t2 = md[2]//3
    md[8] += t2
    md[2] -= t2*3
    min23 = min(md[2],md[3])
    md[6] += min23
    md[3] -= min23
    md[2] -= min23
    return sum([k*v for k,v in md.items()])


timemark()

N = 1000000

ans = [0,0]

for i in range(2,N):
    ans += [mdrs(i)]
    
print(sum(ans))
    
timemark(True)    
