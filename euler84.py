import numpy as np

dim = 40
# 2D6 Dice Dist
# dicedist = [1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]

# 2D4 Dice Dist
dicedist = [1/16,2/36,3/16,4/16,3/16,2/16,1/16]

# CC格转移概率

# 裸转移矩阵

'''
 出现连续3次豹子的期望次数是258次，是马尔科夫链时停，
 状态转移图：
 0H --(1-p)--> 0H
 0H --( p )--> 1H
 1H --(1-p)--> 0H
 1H --( p )--> 2H
 2H --(1-p)--> 0H
 2H --( p )--> 3H
 假设需要x次时停那么有递推方程：
 (1-p)(1+x) + p(1-p)(2+x) + pp(1-p)(3+x) + ppp = x
 
 (1-p)(1+x)   表示T，回到0H状态，次数+1
 p(1-p)(2+x)  表示出HT，回到0H状态，次数+2
 pp(1-p)(3+x) 表示出HHT，回到0H状态，次数+3
 ppp          表示出HHH，结束
 
 求解的 x = (1+p+pp)/ppp
 
 当p=1/6时，x=258

'''

magicrate = 1/258

trx = [[0] * dim for i in range(dim)]
for i in range(dim):
    for j in range(len(dicedist)):
        trx[i][(i+2+j)%dim] = dicedist[j] * (1-magicrate) 
#print(trx[35])
    trx[i][10] += magicrate
mxtrx = np.array(trx)
#print(mxtrx[11,:])





# 30G2J 概率处理
mxpth = np.eye(dim)
mxpth[30,30] = 0
mxpth[30,10] = 1

#CC1
mxpth[2,0] += 1/16
mxpth[2,10] += 1/16
mxpth[2,2] -= 2/16
#CC2
mxpth[17,0] += 1/16
mxpth[17,10] += 1/16
mxpth[17,17] -= 2/16
#CC3
mxpth[33,0] += 1/16
mxpth[33,10] += 1/16
mxpth[33,33] -= 2/16
#CH1
mxpth[7,0] += 1/16
mxpth[7,10] += 1/16
mxpth[7,11] += 1/16
mxpth[7,24] += 1/16
mxpth[7,39] += 1/16
mxpth[7,5] += 1/16
mxpth[7,15] += 2/16
mxpth[7,12] += 1/16
mxpth[7,4] += 1/16
mxpth[7,7] -= 10/16
#CH2
mxpth[22,0] += 1/16
mxpth[22,10] += 1/16
mxpth[22,11] += 1/16
mxpth[22,24] += 1/16
mxpth[22,39] += 1/16
mxpth[22,5] += 1/16
mxpth[22,25] += 2/16
mxpth[22,28] += 1/16
mxpth[22,19] += 1/16
mxpth[22,22] -= 10/16
#CH3
mxpth[36,0] += 1/16
mxpth[36,10] += 1/16
mxpth[36,11] += 1/16
mxpth[36,24] += 1/16
mxpth[36,39] += 1/16
mxpth[36,5] += 1/16
mxpth[36,5] += 2/16
mxpth[36,12] += 1/16
mxpth[36,33] += 1/16
mxpth[36,36] -= 10/16


mxtrx = np.matmul(mxtrx,mxpth)
#print(mxtrx[11,:])


dist = np.array([0] * dim)
dist[0] = 1
dist1 = np.matmul(dist,mxtrx)



for i in range(999999):
    if max(dist-dist1) < 0.000001:
        break
    dist = dist1
    dist1 = np.matmul(dist,mxtrx)
print(dist)
print(dist.argsort()[-3:][::-1])
