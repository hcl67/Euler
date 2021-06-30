
#mxraw = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
#dim = 5


import csv

dim = 80
mxraw = []
with open("p081_matrix.txt") as csvfile:
    x = csv.reader(csvfile)
    for row in x:
        mxraw.append([int(i) for i in row])
        
        
# #print(mxraw[0][0])



def twowaymin(mxraw):
    dim1 = len(mxraw)
    dim2 = len(mxraw[0])
    mxpath = [[0] * dim2 for i in range(dim1)]
    for i in range(dim1):
        for j in range(dim2):
            if i==0 and j==0:
                mxpath[i][j] = mxraw[i][j]
            elif i==0 and j>0:
                mxpath[i][j] = mxraw[i][j] + mxpath[i][j-1]
            elif i>0 and j==0:
                mxpath[i][j] = mxraw[i][j] + mxpath[i-1][j]
            else:
                mxpath[i][j] = mxraw[i][j] + min(mxpath[i][j-1], mxpath[i-1][j])
#print(mxpath)     

    return mxpath[dim1-1][dim2-1]

#初始化mxpath
mxpath = [[0] * dim for i in range(dim)]
for i1 in range(dim):
    for i2 in range(dim):
        if i2 == 0:
            mxpath[i1][i2] = mxraw[i1][i2]
        else:
            mxpath[i1][i2] = mxraw[i1][i2] + mxpath[i1][i2-1]

#print(mxpath)

for i2 in range(1,dim):
    flgind = 1
    while(flgind > 0):
        flgind = 0
        for i1 in range(dim):
            if i1 == 0:
                upath = 99999999
                dpath = mxpath[i1+1][i2]
            elif i1 == dim - 1:
                upath = mxpath[i1-1][i2]          
                dpath = 99999999  
            else:
                upath = mxpath[i1-1][i2]  
                dpath = mxpath[i1+1][i2]
            lpath = mxpath[i1][i2-1]
            newp = min(upath,dpath,lpath)
            if newp + mxraw[i1][i2] < mxpath[i1][i2]:
                mxpath[i1][i2] = newp + mxraw[i1][i2]
                flgind = 1
print(min(mxpath[i][dim-1] for i in range(dim)))
    
       
            
