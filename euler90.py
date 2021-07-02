

def getdice(s):
    if len(s) != 9:
        return 
    d1 = [0,0,0,1,2,3,4,6,8]
    d2 = [1,4,6,6,5,6,6,4,1]
    r1 = [d1[i] if s[i]=='0' else d2[i] for i in range(9)]
    r2 = [d1[i] if s[i]=='1' else d2[i] for i in range(9)]
    return r1,r2

def getpkt(l):
    # l 最少4
    lenl = len(l)
    dgt = [i for i in range(10) if i not in l]
    pool = set()
    if lenl == 6:
        nd = sorted(l)
        pool.add(sum(nd[i]*10**i for i in range(6)))
    elif lenl == 5:
        for i in range(len(dgt)):
            nd = sorted(l+[dgt[i]])
            pool.add(sum(nd[i]*10**i for i in range(6)))     
    elif lenl == 4:
        for i in range(len(dgt)-1):
            for j in range(i+1,len(dgt)):
                nd = sorted(l+[dgt[i],dgt[j]])
                pool.add(sum(nd[i]*10**i for i in range(6))) 
    else:
        print("error: length is not 4/5/6! length is",len(l))
        return
    return pool        
        


tp = set()
for n in range(0,2**8):
    s = format(n,'09b')
#    print(s)
    r1,r2 = getdice(s)
#    print(r1,r2)
    ur1 = list(set(r1))
    ur2 = list(set(r2))
#    print(ur1,ur2)
    if len(ur1) > 6 or len(ur2) > 6:
        continue
    dp1 = getpkt(ur1)
    if 6 in ur1:
        dp1 = dp1.union(getpkt([i if i!=6 else 9 for i in ur1]))
    dp2 = getpkt(ur2)
    if 6 in ur2:
        dp2 = dp2.union(getpkt([i if i!=6 else 9 for i in ur2]))
    for d1 in dp1:
        for d2 in dp2:
            if d1>=d2:
                tp.add(d1*1000000+d2)
            else:
                tp.add(d2*1000000+d1)
print(len(tp))
#print(tp)

    
