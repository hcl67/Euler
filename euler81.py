#mxraw = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
#dim1 = dim2 = 5

_DATA = "p081_matrix.txt"


import csv

dim1 = dim2 = 80
mxraw = []
with open(_DATA) as csvfile:
    x = csv.reader(csvfile)
    for row in x:
        mxraw.append([int(i) for i in row])
        
        
#print(mxraw[0][0])


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

print(mxpath[dim1-1][dim2-1])
       
       
            
