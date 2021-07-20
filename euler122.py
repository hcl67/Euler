m = {1:{frozenset({1})},2:{frozenset({1,2})}}
mmin = [0,1]

k = 200

for i in range(3,k+1):
    print(i)
    mil = []
    for j in range(1,i//2+1):
        for k1 in m[j]:
            for k2 in m[i-j]:
                mil += [k1.union(k2)]
    minl = min(map(len,mil))
    mil = list(filter(lambda x: len(x)<=minl,mil))
    m[i] = set([x.union(frozenset({i})) for x in mil])     
    mmin.append(minl)       
    
    
print(sum(mmin))
