f = open("D:\prime1000000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()

k = 10**10
n = 0

while(1):
    n+=1
    if n%2 == 0:
        continue
    p = plist[n-1]
    s = 2 * p * (n%p)
    if s>k:
        break
    
print(n)
    
