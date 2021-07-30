import math

numlist = [0] * (2000*2000+1)
mat = [[0 for i in range(2000)] for j in range(2000)]



for i in range(2000):
    for j in range(2000):
        k = i*2000+j+1
        if k<=55:
            num = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
        else:
            num = (numlist[k-24] + numlist[k-55] + 1000000) % 1000000 - 500000
        numlist[k] = num
        mat[i][j] = num
        
        
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray. Kadane's algorithm"""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


best_sum = -math.inf

for i in range(2000):
    l = mat[i]
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)

for i in range(2000):
    l = [x[i] for x in mat]
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)

for i in range(2000):
    l = [mat[j][1999-i+j] for j in range(i+1)]   
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)
    
for i in range(2000):
    l = [mat[1999-i+j][j] for j in range(i+1)]   
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)    
    
for i in range(2000):
    l = [mat[j][i-j] for j in range(i+1)]   
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)   
    
for i in range(2000):
    l = [mat[1999-j][1999-i+j] for j in range(i+1)]   
    sub_sum = max_subarray(l)
    best_sum = max(best_sum, sub_sum)    
    
print(best_sum)
