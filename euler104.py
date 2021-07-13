'''
from decimal import Decimal,localcontext



def fib(n):
    y = Decimal.sqrt(Decimal(5))
    return round(1/y*(((1+y)/2)**n-((1-y)/2)**n))

with localcontext() as ctx: 
    ctx.prec = 2000
    print(fib(2749))
'''
import math,datetime

def fibf9(n):
    y = (1+math.sqrt(5))/2
    s = 1/math.sqrt(5)
    for i in range(n):
        s *= y
        if s > 1000000000:
            s /= 10
    return int(s)

btime=datetime.datetime.now()

fib = [0,1,1] 

set9 = {"1","2","3","4","5","6","7","8","9"}

n = 2

while(1):
    n+=1
    l9 = (fib[(n-1)%3] + fib[(n-2)%3]) % 1000000000  
    fib[n%3] = l9
   
    
    if n < 100:
        continue
    l9s = str(l9)
    if set(l9s) == set9:
        print("last",n)
        f9 = fibf9(n)
        f9s = str(f9)
        if set(f9s) == set9:
            print("first&last",n)
            break
    
print(datetime.datetime.now() - btime)  
    
