
import math,datetime
#MXN = 10000
MXN = 1000000000


btime = datetime.datetime.now()
sump = 0

#trail2 利用勾股数生成公式
mn = math.isqrt(MXN//6)+1

def nm2pyth(n,m):
    return [m**2 - n**2, 2*n*m, m**2 +n**2]
 
def isvalid(n,m):
    # n.m为正整数，n>m，n+m=奇数，n和m互质
    return (math.gcd(n,m)==1 and (n+m)%2==1)   

for n in range(1,mn):
    for t in [-1,1]:
        m11 = 3*n*n+t
        if math.isqrt(m11)**2 == m11:
            m = math.isqrt(m11)
            if isvalid(n,m):
                p = 3*(m**2 + n**2) + t
                if p <= MXN:
                    sump += p
            m = m+2*n
            if isvalid(n,m):
                p = 3*(m**2 + n**2) - t
                if p <= MXN:
                    sump += p                
            


'''
#trail1 傻算
#d 是 底边的一半，底边不可能是奇数

MXd = MXN//6
for d in range(2,MXd+1):
    a1 = 3*d*d+1+4*d
    a2 = 3*d*d+1-4*d

    if math.isqrt(a1)**2 == a1:
        sump += 6*d+2
        print('+',d)
#        dl += [d]
    if math.isqrt(a2)**2 == a2:
        sump += 6*d-2
        print('-',d)
#        dl += [d]

'''

    
print(sump)
#print(dl)
print(datetime.datetime.now()-btime)


