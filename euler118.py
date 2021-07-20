from itertools import permutations
import queue


f = open("D:\prime100000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()

def isprime118(n):
    if n == 1:
        return False
    elif n in (2,3,5,7):
        return True
    for p in plist:
        if n%p == 0:
            return False
        elif p*p>n:
            break
    return True



d = ['1','2','3','4','5','6','7','8','9']

ans = set()

for pd in permutations(d):
#for pd in [('2','4','7','5','6','3','1','8','9')]:    
    if pd[8] in ('4','6','8') or pd[8] in ('2','5') and pd[7] in ('4','6','8','0'):
        continue
    dlq = queue.Queue()
    dlq.put([])
    while(not dlq.empty()):
        dl = dlq.get()
        if len(dl) == 0:
            l = 0
        else:
            l = sum(map(len,dl))
        if l == 9:
            ans.add("_".join(sorted(dl)))
#            print(ans)
        d = ''
        for k in range(l,9):
            d += pd[k]
            if len(d) == 1 and d in ('2','3','5','7'):
                dlq.put(dl+[d])
            elif len(d) > 1 and d[-1] in ('2','4','5','6','8'):
                continue
            elif len(d) == 9:
                continue
            elif isprime118(int(d)):
                dlq.put(dl+[d])
                
print(len(ans))       
    
