import math
s = [0] * (500500+1)
t = 0
for k in range(1,500500+1):
    t = (615949*t + 797807) % 2**20
    s[k] = t - 2**19
    
tri = []
n = 1
for i in range(1,1001):
    tri += [s[n:n+i]]
    n += i
    
best_sum = math.inf
sum_list = [0] * 500500   
for i in range(1000):
    x = 0
    for j in range(i,1000):
        for k in range(j-i+1):
            if k == 0:
                tmp_sum = sum(tri[j][k:k+i+1])
            else:
                tmp_sum += - tri[j][k-1]+tri[j][k+i]
            sum_list[x] += tmp_sum
            best_sum = min(best_sum,sum_list[x])
            x += 1

print(best_sum)            
