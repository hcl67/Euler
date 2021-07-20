'''
(a−1)^n + (a+1)^n mod a^2

= (-1)^n + 1 + n*(-1)^(n-1)*a + n*a
= 
2na mod a^2 (if n is odd)
2 mod a^2 (if n is even) 
当a偶数时，rmax = (a-2)a
当a奇数时，rmax = (a-1)a
'''


ans = 0

for a in range(3,1001):
    if a%2 == 1:
        ans += (a-1)*a
    else:
        ans += (a-2)*a
print(ans)
        
        
