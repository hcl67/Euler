'''
对任意数的字母，只许有一个是升序的，必然其余都是降序的，例如 edcba，其组合有C(26,n)种
选定一对字母作为相邻升序组合，如 db->bd 插入剩余字母 eca种，则可插入位置续满足条件：
1.插入点右侧的字幕需小于升序组合右侧的字母；2.插入点左侧的字母续大于升序组合左侧的字母
可见，可插入位置在升序组合原位置的中间，即 pos(d)-pos(b)+1。则对n的字母来说，总共有
sum_{i=1}^{n-1} sum_{j=1}^{i} j = (n-1)n(n+1)/6

发现有遗漏：
badc 中 ad是升序组合，但剩余bc并不保持逆序
所以更严格的场景，升序组合左侧的字母小于其左侧字母，升序组合右侧字母大于其右侧字母即可。两侧可以分别逆序。
可以注意到主要是中间，(pos(d),pos(b))的字母可以放在任意边，可以有2^n种方法
所以公式为：
sum_{i=2}^{n} sum_{j=1}^{i-1} 2^(i-j-1) = 2^n - 1 - n
'''
from math import comb
from itertools import permutations

p = []

for i in range(2,27):
    p += [comb(26,i)*(2**i-1-i)]
    
print(p)
print(max(p))

for p in permutations(['a','b','c','d']):
    fg = 0
    for c in range(len(p)-1):
        if p[c]<p[c+1]:
            fg += 1
    if fg == 1:
        print(p)
    
