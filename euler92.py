import datetime,math


btime = datetime.datetime.now()
MAXN = 10000000

list1 = [1]
list89 = [89]

def e92cal(n):
    s = 0
    for c in str(n):
        s += int(c)**2
    return s


for i in range(1, 1000+1):
    if i in list1 or i in list89:
        continue
    listi = [i]
    ni = e92cal(i)
    while(ni not in list1 and ni not in list89):
        listi += [ni]
        ni = e92cal(ni)
    if ni in list1:
        list1 += listi
    else:
        list89 += listi
   
        
'''
trail 1

cnt1 = 0
cnt89 = 0
cnto = 0
listo = []        
for i in range(1000, MAXN+1):
    if i in list1 or i in list89:
        continue
    ni = e92cal(i)
    if ni in list1:
        cnt1 += 1
    elif ni in list89:
        cnt89 += 1
    else:
        cnto += 1
        listo += [i]
print(len(list89)+cnt89)    
8581146   
'''       
        
cnt89 = 0
for i1 in range(10):
    for i2 in range(i1, 10):
        for i3 in range(i2, 10):
            for i4 in range(i3,10):
                for i5 in range(i4,10):
                    for i6 in range(i5,10):
                        for i7 in range(i6,10):
                            dgt = [i1,i2,i3,i4,i5,i6,i7]
                            dgts2 = sum(i**2 for i in dgt)
                            dgtnum = math.factorial(7)
                            dgtdict = {}
                            for d in dgt:
                                if d in dgtdict:
                                    dgtdict[d]+=1
                                else:
                                    dgtdict[d]=1
                            dgtdictcnt2 = [i for i in list(dgtdict.values()) if i > 1]
                            for i in dgtdictcnt2:
                                dgtnum = dgtnum//math.factorial(i)
                            if dgts2 in list89:
                                cnt89+=dgtnum
print(cnt89)                            

print(datetime.datetime.now() - btime)
