'''
Project Euler Problem #15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.


How many routes are there through a 20x20 grid?
'''
x=20
k=[[1 for i in range(x+1)] for j in range(x+1)]

for i in range(1,x+1):
    for j in range(1,x+1):
        k[i][j]=k[i-1][j]+k[i][j-1]
print(k[x][x])
