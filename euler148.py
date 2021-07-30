'''
类似与谢尔宾斯基三角形（英语：Sierpinski triangle）

0~6 构成的被7除不尽的三角形
在7n+i  n<7 i=0~6 中间重复，n层重复n次
之后
0~48 构成的被7除不尽的三角形
在49n+i  n<7 i=0~48 中间重复，n层重复n次

以此类推 


'''
import math    

ans = 28
N = 100
#for i in range(7,N+1):

n = 10**9  #层数 = 数 - 1

def s148(n):
    return sum(0 if math.comb(n-1,i)%7 == 0 else 1 for i in range(n))
    


def l148(n):
    
    k = int(math.log(n,7)) + 1
    layer = []
    for i in range(k):
        layer += [n%7]
        n //= 7
    return layer[::-1]

def c148(n):
    layer = l148(n)
    lenth = len(layer)
    ans = (layer[0]+1)*layer[0]//2
    cnt = layer[0]+1
    for i in range(1,lenth):
        ans *= 28
        ans += cnt*(layer[i]+1)*(layer[i])//2
        cnt *= layer[i]+1
    return ans

print(c148(n))
       
    


    


