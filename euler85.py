def cntr(a,b):
    return ((1+a)*a//2) * ((1+b)*b//2) 
    


#print(cntr(59,59))

ans = (59,59)
dff = abs(cntr(ans[0],ans[1]) - 2000000)

for a in range(1,60):
    b = a
    while(cntr(a,b)<=2000000):
        a += 1
    d1 = abs(cntr(b,a-1) - 2000000)
    d2 = abs(cntr(b,a) - 2000000)
    if d1 <= d2 and d1 < dff:
        ans = (b, a-1)
        dff = d1
    elif d2 < d1 and d2< dff:
        ans = (b, a)
        dff = d2

print(ans)
print(ans[0]*ans[1])
print(cntr(ans[0], ans[1]))
    
