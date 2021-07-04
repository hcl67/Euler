import itertools,datetime

def getop(d1,d2,o):
    if o == '+':
        return d1 + d2
    elif o == '-':
        return d1 - d2
    elif o == '*':
        return d1 * d2
    elif o == '/':
        if d2 == 0:
            return 9999999999
        return d1 / d2
    else:
        raise Exception("error on getop")
    return

op = ['+','-','*','/']
opl = []
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            opl +=[(op[i1],op[i2],op[i3])]


#dl = [(1,2,3,4)]
dl = list(itertools.combinations(range(10), 4))

dd = {}
for d in dl:
    ds = set()
    dpl = list(itertools.permutations(d))
    for dp in dpl:
        for o in opl:
            t1 = getop(dp[0], dp[1], o[0])
            t2 = getop(t1, dp[2], o[1])
            t3 = getop(t2, dp[3], o[2])
            if int(t3) == t3:
                ds.add(t3)
            t1 = getop(dp[2], dp[3], o[0])
            t2 = getop(dp[1], t1, o[1])
            t3 = getop(dp[0], t2, o[2])
            if int(t3) == t3:
                ds.add(t3)
            t1 = getop(dp[0], dp[1], o[0])
            t2 = getop(dp[2], dp[3], o[1])
            t3 = getop(t1, t2, o[2])
            if int(t3) == t3:
                ds.add(t3)
    dsl = sorted([i for i in list(ds) if i > 0])
    dsl2 = [i+1 for i in range(len(dsl)) if i+1 == dsl[i]]
    dd[d] = len(dsl2)
    
maxd = max(dd.items(), key=lambda x: x[1])
print(maxd)
print(dd)
