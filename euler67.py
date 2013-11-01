'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

data=open("triangle.txt")
k=[]
for line in data:
    k.append([int(x) for x in line.rstrip("\n").split(" ")])

#print(k)
    

for i in range(99):
    for j in range(99-i):
        k[98-i][j]+=max(k[99-i][j],k[99-i][j+1])
print(k[0][0])

