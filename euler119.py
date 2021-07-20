d = 5
p = 2

n = []

k = 30
dcap = 1000
pdcap = 10**30

while(d < dcap):
    while(pow(d,p) < 10):
        p += 1
    pd = pdi = pow(d,p)
    sumpd = 0
    while(pdi > 0):
        sumpd += pdi % 10
        pdi = pdi // 10
    if sumpd == d:
        n += [(d,p,pd)]
        p += 1
    elif pd > pdcap:
        p = 2
        d += 1
    else:
        p += 1

print(sorted(n,key = lambda x:x[2])[:k])
