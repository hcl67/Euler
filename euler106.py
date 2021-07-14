'''
n个数一分二后无严格大于性保证的分组数，无需比较当且仅当2保续分组中，同序号的元素都保持同样的大小关系

  n = 4 : 1
  n = 6 : 5   推断方式，n个数1.固定n[0]   ,n[-1]
  n = 8 :   
      
'''

from itertools import combinations
from math import comb

def getoddnum(n):   #返回n个数一分二后的组合数
    if n%2 == 1:
        return -99999999
    nlist = list(range(n))
    sublist = combinations(nlist[1:], n//2 - 1)
    ans = 0
    for s in sublist:
        suba = sorted([0] + list(s))
        subb = sorted(list(set(nlist) - set(suba)))
        k = 0
        
        for i in range(n//2):
            if suba[i] > subb[i]:
                k += 1
            elif suba[i] < subb[i]:
                k -= 1
        if abs(k) < n/2:
#            print(suba,subb)
            ans += 1
    return ans

def getnum(n):
    ans = 0
    checklist = [4 + i*2 for i in range((n-2)//2)]
    for i in checklist:
        ans += comb(n,n-i)*getoddnum(i)
        
    return ans
    



print(getnum(4))
print(getnum(7))
print(getnum(12))
