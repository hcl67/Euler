

'''
正的：
f(n,m) = m*(m+1)*n*(n+1)/4

斜的：
(m>n)
g(n,m) = g(n,n)+(m-n)*(sum(i*(n*2-i) for i in range(1,n*2)))
g(n,n) = sum(f(2*i,2*n-2*i) for i in range(1,n)) - sum(f(2*i,2*n-2-2*i) for i in range(1,n-1))


'''



from datetime import datetime 
btime = datetime.now()




def f147(m,n):
    return m*(m+1)*n*(n+1)//4

def g147(m,n):
    if m == n:
        if n == 1:
            return 0
        else:
            return sum(f147(2*i,2*n-2*i) for i in range(1,n)) - sum(f147(2*i,2*n-2-2*i) for i in range(1,n-1))
    elif m<n:
        m,n = n,m
    return g147(n,n) + (m-n)*(sum(i*(n*2-i) for i in range(1,n*2)))
    


ans = 0

m,n = 47,43


for i in range(1,m+1):
    for j in range(1,n+1):
        ans += f147(i,j) + g147(i,j)


print(ans)


print(datetime.now() - btime)
