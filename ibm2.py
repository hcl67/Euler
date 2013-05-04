p=[2,3,5,7,11,13]
d=[8,1,9,4,4,4]
for i in range(6):
    for j in range(d[i]):
        s=0
        for k in range(6):
            if k==i:
                s^=d[k]-j-1
            else:
                s^=d[k]
        if s==0:
            print(p[i],j+1,p[i]**(j+1))
