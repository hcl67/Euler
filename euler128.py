from datetime import datetime
btime=datetime.now()

'''
每圈的元素可分为头尾，角，边
对于边而言，相邻的数为：
[num-lastrnd-i-1,num-lastrnd-i,num-1,num+1,num+rnd+i,num+rnd+i+1]
差值为
[lastrnd+i+1,lastrnd+i,1,1,rnd+i,rnd+i+1]
lastrnd+i+1与lastrnd+i,rnd+i与rnd+i+1 至多只有1个质数，故边的质数必<=2，可以跳过

对于角而言，相邻的数为：
[num-lastrnd-i,num-1,num+1,num+rnd+i,num+rnd+i-1,num+rnd+i+1]
差值为
[lastrnd+i,1,1,rnd+i,rnd+i-1,rnd+i+1]
注意到 rnd = lastrnd + 6，则lastrnd+i与rnd+i同奇偶，rnd+i-1与rnd+i+1同奇偶，故角的质数必<=2，可以跳过



'''
  
f = open("d:\prime100000.txt", "r")
plist = []
for line in f:
    plist += list(map(int,line.rstrip("\n").split(" ")))
f.close()



def isprime(n):
    if n == 1:
        return False
    for p in plist:
        if p*p>n:
            break
        elif n%p == 0:
            return False
    return True

p3dict = {1:[2,3,4,5,6,7],2:[8,9,3,1,7,19]}
p3list = [1,2]
thrd = 2000

n = 1
while (len(p3list)<thrd):
    n+=1   
    #圈起点
    num = 2+n*(n-1)*3
#    dpnum = [6*n-1,6*n+1,12*n+5]
    if isprime(6*n-1) and isprime(6*n+1) and isprime(12*n+5):
        p3list += [num]
        print(len(p3list))
    #圈终点
    num = 1+n*(n+1)*3
#    dpnum = [12*n-7,6*n-1,6*n+5]
    if isprime(6*n-1) and isprime(6*n+5) and isprime(12*n-7):
        p3list += [num]   
        print(len(p3list))



'''
n = 1
base = 2
rnd = 6
nextbase = 8
nextrnd = 12
while (len(p3list)<thrd):
    n += 1
    lastbase = base
    lastrnd = rnd
    base = nextbase
    rnd = nextrnd
    nextbase = base + rnd
    nextrnd = rnd + 6
    for i in range(6):
        for j in range(n):
            num = base + n*i + j
            if i == 0 and j == 0:
                pnum = [lastbase, num+1, num+rnd-1,nextbase,nextbase+1,nextbase+nextrnd - 1]
            elif j == 0:
                pnum = [num-lastrnd-i,num-1,num+1,num+rnd+i,num+rnd+i-1,num+rnd+i+1]
            elif i == 5 and j == n-1:
                pnum = [lastbase,num-lastrnd-i-1,num-1,base,num+rnd+i,num+rnd+i+1]
            else:
                pnum = [num-lastrnd-i-1,num-lastrnd-i,num-1,num+1,num+rnd+i,num+rnd+i+1]
            dpnum = [abs(x-num) for x in pnum]
            if isprime3(dpnum):
                p3dict[num] = pnum 
                p3list += [num]
                print(n,i,j,num)
'''

print(p3list[-1])     
print(datetime.now()-btime)       
                
                
            
    
