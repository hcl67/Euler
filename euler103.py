from itertools import combinations

n1 = {1}
n2 = {1, 2}
n3 = {2, 3, 4}
n4 = {3, 5, 6, 7}
n5 = {6, 9, 11, 12, 13}
n6 = {11, 18, 19, 20, 22, 25}

n7 = {20, 31, 38, 39, 40, 42, 45}

'''
基本分析
由于任意2个的和要不等，所以连续数字间隔至少要是1123...(后面的未知)

'''

def check103(nset, printflag = True):
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

        
       

#print(check103(n7))

n7best = set({999,998,997,996,995,994,993})

for i7 in range(60,43,-1):
#    print(i7)
    for i6 in range(i7-1,24,-1):
        for i5 in range(i6-1,23,-1):
            for i4 in range(i5-1,22,-1):
                for i3 in range(i4-1,21,-1):
                    for i2 in range(i3-1,20,-1):
                        for i1 in range(i2-1,19,-1):
                            n7cand={i1,i2,i3,i4,i5,i6,i7}
                            #print(n7cand)
                            if check103(n7cand, printflag = False):
                                if sum(n7cand) < sum(n7best):
                                    n7best = n7cand
                                #print(n7cand)
                                #print(sum(n7cand))
    print("best n7 for i7 = ", i7, ":", n7best, "sum=",sum(n7best))        
print("allbest n7", n7best, "sum=",sum(n7best))
