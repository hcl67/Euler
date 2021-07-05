import datetime,math

#BIGN = 100000
btime = datetime.datetime.now()
BIGN = 1000000

from functools import reduce


def getdiv(n):
    divset = {1}
    step = n%2+1
    for i in range(step+1,math.isqrt(n)+1,step):
        if not n%i:
            divset.add(i)
            divset.add(n//i)
    return divset
    

def getsumdiv(n):
    return sum(getdiv(n))

check = {}

 


#trial 1
txn = [getsumdiv(i) for i in range(BIGN+1)]

for i in range(2,BIGN+1):

    if i==12496:
        print(i)
    n = txn[i]
    if n <= 0:
        continue
    chain = {i}
    chainl = [i]
    while(1):
        if n > BIGN:
            tgt = 0
            break
        elif n == 1:
            tgt = 1
            break
        elif n <= 0:
            tgt = -n
            break
        elif n in chain:
            tgt = n
            check[tgt] = len(chain) - chainl.index(n)
            break
        else:
            chain.add(n)
            chainl += [n]
            n = txn[n]
    for k in chain:
        txn[k] = -tgt
      
#print([(i,num[i]) for i in range(len(num))])        
print(check)
print(datetime.datetime.now()-btime)

