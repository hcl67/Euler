from itertools import combinations
from math import factorial,prod

c = list(range(1,16))

ans = 1
for k in range(1,8):
    for cb in combinations(c,k):
        ans += prod(cb)
    
print(int(factorial(16)/ans))
    
