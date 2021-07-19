
m = 50
k = 50


'''
def cal115(m,k):
    rblk = [0]*m + [1]
    
    for i in range(m+1,k+1):
        rblk.append(sum((j-m)*rblk[i-j]+1 for j in range(m+1,i+1))+1)
        
    blk = sum(rblk)+1    
    return blk            

'''
rblk = [0]*m + [1]

    
    
blk = sum(rblk)+1     
while(1):
    k+=1
    rblk.append(sum((j-m)*rblk[k-j]+1 for j in range(m+1,k+1))+1)    
    if sum(rblk)+1  > 1000000:
        print(k)
        break
    

