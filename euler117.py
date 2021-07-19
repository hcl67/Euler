k = 50



d = [1,1,2,4,8]



for i in range(5,k+1):
    d.append(d[-4]+d[-3]+d[-2]+d[-1])
    
print(d[-1])
