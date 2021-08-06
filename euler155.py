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
        
timemark()


from collections import defaultdict
from math import gcd


N = 18   #可用电容数

cpdict = defaultdict(set)
cpdict[1] = {(1,1)}
cpfull = {(1,1)}
for n in range(2,N+1):
    cpn = set()
    for i in range(1,n//2+1):
        j = n-i
        for x in cpdict[i]:
            for y in cpdict[j]:
                b,a = x
                d,c = y
                na,nd,nbc = a*c,b*d,a*d+b*c
                gcd1=gcd(na,nbc)
                gcd2=gcd(nd,nbc)
                cpn.update({(nbc//gcd1,na//gcd1),(nd//gcd2,nbc//gcd2)})
    cpn.difference_update(cpfull)
    cpdict[n] = cpn
    cpfull.update(cpn)

print(len(cpfull))

timemark(True)
