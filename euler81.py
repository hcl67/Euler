
#mxraw = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
#dim = 5


import csv

dim = 80
mxraw = []
with open("p081_matrix.txt") as csvfile:
    x = csv.reader(csvfile)
    for row in x:
        mxraw.append([int(i) for i in row])
        
        
#print(mxraw[0][0])


mxpath = [[0] * dim for i in range(dim)]
mxpath[0][0] = mxraw[0][0]
for n in range(1,dim):
    for j in range(n+1):
        if j==0:
            mxpath[j][n-j] = mxraw[j][n-j] + mxpath[j][n-j-1]
        elif j==n:
            mxpath[j][n-j] = mxraw[j][n-j] + mxpath[j-1][n-j]
        else:
            mxpath[j][n-j] = mxraw[j][n-j] + min(mxpath[j][n-j-1],mxpath[j-1][n-j])
#print(mxpath)     
for n in range(1,dim):
    for j in range(dim-n):
        mxpath[dim-1-j][j+n] = mxraw[dim-1-j][j+n] + min(mxpath[dim-1-j-1][j+n] ,mxpath[dim-1-j][j+n-1] )

print(mxpath[dim-1][dim-1])
       
            
