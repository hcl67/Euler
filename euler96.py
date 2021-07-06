import datetime,copy
import numpy as np
from functools import reduce

MAXITER = 10000

sdklst = []
f = open("p096_sudoku.txt", "r")
for line in f:
    if "Grid" in line:
        readflag = 0
        sdk = []
    else:
        sdkline = list(map(int,list(line.rstrip("\n"))))
        sdk.append(sdkline)
        readflag += 1
        if readflag == 9:
            sdklst.append(sdk)
f.close()

sdkrowlst = []
for i in range(9):
    sdkrow = []
    for j in range(9):
        sdkrow.append((i,j))
    sdkrowlst.append(sdkrow)
#print(sdkrowlst)

sdkcollst = []
for j in range(9):
    sdkcol = []
    for i in range(9):
        sdkcol.append((i,j))
    sdkcollst.append(sdkcol)
#print(sdkcollst)

sdkblklst = []
for i1 in range(3):
    for j1 in range(3):
        sdkblk = []
        for i2 in range(3):
            for j2 in range(3):
                sdkblk.append((i1*3+i2,j1*3+j2))
        sdkblklst.append(sdkblk)
#print(sdkblklst)

def ninecheck(lst):
    # 判断9个数中有没有非零的重复数字
    if len(lst) != 9:
        return False
    lst1 = list(filter(lambda x:x>0, lst))
    return len(lst1) == len(set(lst1))

def sdkgetrow(sdk,cell,sel):
    # 返回sdk中cell对应的行(r)列(c)块(b)
    i = cell[0]
    j = cell[1]
    if sel == 'r':
        return [sdk[tp[0]][tp[1]] for tp in sdkrowlst[i]]
    elif sel == 'c':
        return [sdk[tp[0]][tp[1]] for tp in sdkcollst[j]]
    elif sel == 'b':
        return [sdk[tp[0]][tp[1]] for tp in sdkblklst[i//3*3+j//3]]
    else:
        return [0]*9


def sdkvalid(sdk, cell = (-1,-1)):
    # 若cell非(-1,-1)则判断cell对应的行列块是否合法，不然判断全数独是否合法
    if cell != (-1,-1):
        r = ninecheck(sdkgetrow(skd,cell,'r'))
        c = ninecheck(sdkgetrow(skd,cell,'c'))
        b = ninecheck(sdkgetrow(skd,cell,'b'))
    else:
        r = reduce((lambda x,y: x and y), [ninecheck([sdk[tp[0]][tp[1]] for tp in sdkrowlst[n]]) for n in range(9)])
        c = reduce((lambda x,y: x and y), [ninecheck([sdk[tp[0]][tp[1]] for tp in sdkcollst[n]]) for n in range(9)])
        b = reduce((lambda x,y: x and y), [ninecheck([sdk[tp[0]][tp[1]] for tp in sdkblklst[n]]) for n in range(9)])
    return r and c and b
        
def sdkcomplete(sdk):
    # 判断数独是否已经完成
    for i in range(9):
        for j in range(9):
            if sdk[i][j] == 0:
                return (i,j)
    return (-1,-1)

def sdkgetvalid(sdk,cell):
    # 根据cell位置，获取该cell的候选数字
    vld = set()
    flst = set(range(1,10))
    if sdk[cell[0]][cell[1]] > 0:
        return vld
    else:
        vldr = flst.difference(set(sdkgetrow(sdk,cell,'r')))
        vldc = flst.difference(set(sdkgetrow(sdk,cell,'c')))
        vldb = flst.difference(set(sdkgetrow(sdk,cell,'b')))
        vld = set.intersection(vldr, vldc, vldb)
        return vld
        

def sdkfill(sdk):
    # 根据规则简单填充数独
    newsdk = copy.deepcopy(sdk)
    updateflg = 1
    while(updateflg):
        updateflg = 0
        for i in range(9):
            for j in range(9):
                if newsdk[i][j]>0:
                    continue
                else:
                    vld= sdkgetvalid(newsdk,(i,j))
                    if len(vld) == 0:
                        return newsdk,0
                    elif len(vld) == 1:
                        newsdk[i][j] = vld.pop()
                        updateflg = 1
    return newsdk,1
                    

def sdkguess(sdk0,cell):
    sdk1 = copy.deepcopy(sdk0)
    cellvld = sdkgetvalid(sdk1,cell)
    if len(cellvld) == 0:
        return sdk1,0
    for d in cellvld:
        sdk1[cell[0]][cell[1]] = d
        sdk2,s = sdkfill(sdk1)
        if not s:
            continue
        nextcell = sdkcomplete(sdk2)
        if nextcell == (-1,-1):  
            return sdk2,1
        else:
            sdk2,s = sdkguess(sdk2,nextcell)
            if s == 1:
                return sdk2,s
            else:
                continue
    return sdk2,0
        
sdkdlst = []
sumlst = []
it = 0
for sdk in sdklst:
    # 1. 根据规则推断填充数独并判断是否完成数独
    newsdk,s = sdkfill(sdk)
    nextcell = sdkcomplete(newsdk)
    if nextcell != (-1,-1):
        # 2. 猜测
        newsdk,s = sdkguess(newsdk,nextcell)
    sdkdlst.append(newsdk)
    sumlst.append(newsdk[0][0]*100+newsdk[0][1]*10+newsdk[0][2])
print(sdkdlst)
print(sumlst)
print(sum(sumlst))
    
      
