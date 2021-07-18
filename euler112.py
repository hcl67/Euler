    
    
def isbcn(n):
    sn = str(n)
    if len(sn) == 1:
        return 0
    cl = [int(sn[i]) - int(sn[i+1]) for i in range(len(sn)-1)]
    if min(cl) < 0 and max(cl) > 0:
        return 1
    else:
        return 0
    

    

bcnt = 0
thrd = 0.99
n = 1
while(1):
    bcnt += isbcn(n)
    if bcnt/n >= thrd:
        break
    n += 1

    
print(n,bcnt)
