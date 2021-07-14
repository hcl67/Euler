  
from itertools import combinations

def check105(nset, printflag = False):
    minsumlist = [0]
    maxsumlist = [0] 
    for l in range(1,len(nset)+1):
        subsetlist = combinations(nset, l)
        sumcheck = [sum(i) for i in subsetlist]
        minsumlist.append(min(sumcheck))
        maxsumlist.append(max(sumcheck))

        # check 1 对任意2个个数相等的不交集合，和不同
        if len(sumcheck) != len(set(sumcheck)):
            if printflag:
                print("check1 failed at l = ", l)
                print("sumcheck :",sumcheck )
            return False
        # check 2 对任意2个个数不相等的不交集合，个数多的和大
        if minsumlist[-1] <= maxsumlist[-2]:
            if printflag:
                print("check2 failed at l = ", l)
                print("min = ", minsumlist[-1], ", lastmax = ", maxsumlist[-2])
            return False
    return True


f = open("D:\p105_sets.txt", "r")
setlist = []
for line in f:
    setlist += [set(map(int,line.rstrip("\n").split(",")))]
f.close()

ans = 0
for numset in setlist:
    if check105(numset):
        ans += sum(numset)
print(ans)
