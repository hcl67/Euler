k = 50

d2 = [0,0,1]

for i in range(3,k+1):
    d2.append(d2[-2]+1+d2[-1])
    
d3 = [0,0,0,1]

for i in range(4,k+1):
    d3.append(d3[-3]+1+d3[-1])

d4 = [0,0,0,0,1]

for i in range(5,k+1):
    d4.append(d4[-4]+1+d4[-1])
    
print(d2[-1],d3[-1],d4[-1],d2[-1]+d3[-1]+d4[-1])
