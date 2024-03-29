'''
易知，在池内1/v的小池内，Swimer(S)有绝对优势，故总能达成Walker(W)与S有最远距离的情形，如例题1中，S在(-1/v,0) W在(1,0)。之后计算S以最优路线逃脱所需时间，用于迭代需要的v。
若将S的速度分为径向速度r，即面对池边的脱离方向；与切向速度p，即与W运动相同的方向，易知，r与l垂直，r^2+p^2 = 1。同时，p越快，W追击的时间越久，相对的W的追击速度越慢，相对的S的径向速度越快。
同时，对于W的追击而言，S离池心的距离越远，p带来的效果越小。
例题1中，当S距离池心的距离是l的时候，p带给W的追击效果位p/l，即W的速度相对变为(v-p/l)=v(1-p/vl)，即相对的S得径向速度r提升1/(1-p/vl)，称为相对r(rr)。
如何确定p的问题改为求解最优化问题 sqrt(1-p^2)/(1-p/vl)。此问题当l>1/v时的最优解位p=1/vl，即在l位置时，rr的最优解位1/sqrt(1-1/(vl)^2)。
则当S的径向从1/v到1的过程积分即可的脱离时间，积分dl/rr => 积分sqrt(1-1/(vl)^2)dl 
为 (sqrt((v*l)**2-1)-atan(sqrt((v*l)**2-1)))/v，带入上下界可求的v对应的脱离时间t，基于脱离时间迭代W速度为pi/t，通过反复迭代可求的v
例题2中，推断上述时间计算基本应该无差别，但主义S通过对角线时，可以采取旋转90度的策略让W增加运动路线，暂未求出最终解；
经思考，认为转角是必须的，并不会让W增加运动路线，考虑S的初始位置是否可能通过某种方式达到离边缘更近的位置，然而即便是可能S按圆形的行动，也未得出原题结论
'''

import math

def inte(x,v):
    y = math.sqrt(max((v*x)**2-1,0))
    return (y-math.atan(y))/v  

#例题1
v = math.pi
while(1):

    t = inte(1,v) - inte(1/v,v)
    newv = math.pi/t
#    print(v)
    if abs(newv-v) < 1e-10:
        break
    v = newv
#print(v)  

#例题2
v = 4
while(1):

    t = inte(1,v) - inte(4/v/math.pi,v)
    newv = 4/t
#    print(v)
    if abs(newv-v) < 1e-10:
        break
    v = newv
print(v) 
print()
v = 4
while(1):

    t = inte(1,v) - inte(2/v,v)
    newv = 4/t
#    print(v)
    if abs(newv-v) < 1e-10:
        break
    v = newv
print(v) 
