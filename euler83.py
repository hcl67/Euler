
# mxraw = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
# dim = 5


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
for i in range(dim):
    for j in range(dim):
        if i==0 and j==0:
            mxpath[i][j] = mxraw[i][j]
        elif i==0 and j>0:
            mxpath[i][j] = mxraw[i][j] + mxpath[i][j-1]
        elif i>0 and j==0:
            mxpath[i][j] = mxraw[i][j] + mxpath[i-1][j]
        else:
            mxpath[i][j] = mxraw[i][j] + min(mxpath[i][j-1], mxpath[i-1][j])

# print(mxpath)


flgind = 1
while(flgind > 0):
    flgind = 0
    for i in range(dim):
        for j in range(dim):    
            if i == 0:
                upath = 99999999
            else:
                upath = mxpath[i-1][j]  
            if i == dim - 1:
                dpath = 99999999
            else:
                dpath = mxpath[i+1][j]
            if j == 0:
                lpath = 99999999
            else:
                lpath = mxpath[i][j-1]
            if j == dim - 1:
                rpath = 99999999
            else:
                rpath = mxpath[i][j+1]
            newp = min(upath,dpath,lpath,rpath)
            if newp + mxraw[i][j] < mxpath[i][j]:
                mxpath[i][j] = newp + mxraw[i][j]
                flgind = 1
print(mxpath[dim-1][dim-1])
    
       
            
