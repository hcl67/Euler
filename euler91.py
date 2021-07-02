MAXN = 50

tot = 0
xylist = []
for i in range(MAXN+1):
    for j in range(MAXN+1):
        if i==0 and j==0:
            continue
        xylist += [(i,j)]
      
        
lenxylist = len(xylist)         
for i in range(lenxylist-1):
    for j in range(i+1, lenxylist):
        x = xylist[i]
        y = xylist[j]
        l1 = x[0]**2 + x[1]**2
        l2 = y[0]**2 + y[1]**2
        l3 = (x[0]-y[0])**2 + (x[1]-y[1])**2
        llist = sorted([l1,l2,l3])
        if llist[0] + llist[1] == llist[2]:
            tot += 1 
            
print(tot)
