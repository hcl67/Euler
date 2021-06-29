from decimal import Decimal, getcontext
from math import sqrt

getcontext().prec = 105

tot = 0
for num in range(1,101):
    if int(sqrt(num))**2 == num:
        continue
    x = Decimal(sqrt(num))
    x1 = (x+Decimal(num)/x)/Decimal(2)
#    print(x,x1)

    while(abs(x1-x)>1e-105):
        x = x1
        x1 = (x+Decimal(num)/x)/Decimal(2)

    d100 = str(x).replace('.','')[:100]
#    print(d100)
    ts = sum([int(d) for d in d100])
    tot += ts
print(tot)
