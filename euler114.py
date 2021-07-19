rblk = [0,0,0,1]

k = 50

for i in range(4,k+1):
    rblk.append(sum((j-3)*rblk[i-j]+1 for j in range(4,i+1))+1)
    
                
    
blk = sum(rblk)+1                
print(blk)
