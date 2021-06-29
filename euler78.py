import math
maxn = 100000
maxk = int((math.sqrt(maxn*24+1)+1)/6)
klist = []
for k in range(1,maxk+1):
    klist.append(int((-1)**(k+1) * k*(3*k-1)/2))
    klist.append(int((-1)**(-k+1) * -k*(-3*k-1)/2))

#print(klist)
    

p = [1,1]


for n in range(2, maxn+1):
    tp = 0
    for k in klist:
        if abs(k) > n:
            break
        elif k>0:
            tp += p[n-k]
        elif k<0:
            tp -= p[n+k]
        else:
            print("error")
        tp = tp % 1000000
    if tp == 0:
        print(n)
        break
    p.append(tp)
 
print(n,tp)

    
