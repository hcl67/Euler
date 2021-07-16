
f = open("d:\p107_network.txt", "r")
mx = []
for line in f:
    mx += [list(map(lambda x:0 if x=='-' else int(x),line.rstrip("\n").split(",")))]
f.close()
'''

mx = [[ 0,16,12,21, 0, 0, 0],
      [16, 0, 0,17,20, 0, 0],
      [12, 0, 0,28, 0,31, 0],
      [21,17,28, 0,18,19,23],
      [ 0,20, 0,18, 0, 0,11],
      [ 0, 0,31,19, 0, 0,27],
      [ 0, 0, 0,23,11,27, 0]]
'''

edge = {}
for i in range(len(mx)-1):
    for j in range(i+1,len(mx)):
        edge[(i,j)] = mx[i][j]
        
edge = dict(sorted(edge.items(), key = lambda x:x[1]))
        
print(sum(edge.values()))

dus = list(range(len(mx)))

def getdus(dus,n):
    if dus[n] == n:
        return n
    else:
        dus[n] = getdus(dus,dus[n])
        return dus[n]
    
def upddus(dus,n,val):
    if dus[n] == n:
        dus[n] = val
        
    else:
        upddus(dus,dus[n],val)
        dus[n] = val
    return
    

tot = 0
for k,v in edge.items():
    if v == 0:
        continue
    k0 = getdus(dus,k[0])
    k1 = getdus(dus,k[1])
    if k0 != k1:
        mink = min(k0,k1)
        upddus(dus,k[0],mink)
        upddus(dus,k[1],mink)
        tot += v
        print(k,v)

print(tot)

print(sum(edge.values())-tot)
