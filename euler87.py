import math,datetime

BDY = 50000000

my_file = open("Prime10000000.txt", "r")
content = my_file.read()
plist = content.split(" ")
my_file.close()

pow2 = []
pow3 = []
pow4 = []

flg3 = 0
flg4 = 0 

for sp in plist:
    p = int(sp)
    p2 = p*p
    if p2 > BDY:
        break
    pow2.append(p2)
    if flg3 == 0:
        p3 = p**3
        if p3 > BDY:
            flg3 = 1
        else:
            pow3.append(p3)
    if flg4 == 0:
        p4 = p**4
        if p4 > BDY:
            flg4 = 1
        else:
            pow4.append(p4)
            
            
numset = set()
for p2 in pow2:
    for p3 in pow3:
        if p2 + p3 > BDY:
            break
        for p4 in pow4:
            if p2 + p3 + p4 > BDY:
                break
            numset.add(p2+p3+p4)
print(len(numset))
            
    
        

        
