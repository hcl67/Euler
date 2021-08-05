# 50分钟
timestamp = []

def timemark(printflag = False):
    from datetime import datetime
    global timestamp
    ts = datetime.now()
    if len(timestamp) == 0:
        timestamp = [ts]
    else:    
        timestamp[-1] = ts - timestamp[-1]
        timestamp += [ts]
    if printflag:
        for i in range(len(timestamp)-1):
            print(timestamp[i])
        timestamp = []
    return 
        
timemark()
def pnp(n,p):  #含p量
    if p == 1:
        return n
    r = 0
    pp = p
    while pp <= n:
        r += n//pp
        pp *= p
    return r

def pmnp(m,n,p):
    return pnp(m,p) - pnp(m-n,p)

def cmnp(m,n,p):
    return pnp(m,p)- pnp(m-n,p) - pnp(n,p)
    
def cmnnp(m,n1,n2,p):
    return pnp(m,p) - pnp(m-n1-n2,p) - pnp(n1,p) - pnp(n2,p)

#print(cmnp(200000,10,2))
#print(cmnnp(200000,5,5,2))


p25dict = {}
for i in range(200000+1):
    p25dict[i] = (pnp(i,2),pnp(i,5)) 
    


N = 200000
tgt = 12
tgt2 = p25dict[N][0] - tgt
tgt5 = p25dict[N][1] - tgt

timemark()

ans = 0
for i in range(0,N//3+1):
    for j in range(i,(N-i)//2 + 1):
        k = N-i-j
        if p25dict[i][0] + p25dict[j][0] + p25dict[k][0] <= tgt2 and p25dict[i][1] + p25dict[j][1] + p25dict[k][1] <= tgt5:
            if i == j == k:
                p = 1
            elif i == j or i == k or j == k:
                p = 3
            else:
                p = 6
            ans += p

print(ans)


'''
timemark()

ans = 0
for i in range(0,N+1):
    for j in range(0,i+1):
        if p25dict[N-i][0] + p25dict[i-j][0] + p25dict[j][0] <= tgt2 and p25dict[N-i][1] + p25dict[i-j][1] + p25dict[j][1] <= tgt5:
            ans += 1

print(ans)
'''
'''
C(n,n-k)C(n-k,j+1) + C(n,n-k-1)C(n-k-1,j) + C(n,n-k-1)C(n-k-1,j+1) = C(n+1,k+1)C(n-k,j+1)

C(n,k) + C(n,k+1) = C(n+1,k+1)

'''
        
# print(ans)
    
#print(cmnnp(200000,15621,12505,2))
#print(cmnnp(200000,15621,12505,5))

#print(cmnnp(3,1,1,6))


timemark(True)
