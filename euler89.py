import math,datetime,sys




rmnlst = []
f = open("p089_roman.txt", "r")
for line in f:
    rmnlst.append(line.rstrip('\n'))
f.close()


# rmnlst = ['MMMMDCLXXII',
#  'MMDCCCLXXXIII',
#  'MMMDLXVIIII',
#  'MMMMDXCV',
#  'DCCCLXXII',
#  'MMCCCVI',
#  'MMMCDLXXXVII',
#  'MMMMCCXXI',
#  'MMMCCXX',
#  'MMMMDCCCLXXIII']

'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''

def getrmnc(c):
    if c=='I':
        return 1
    elif c=='V':
        return 5
    elif c=='X':
        return 10
    elif c=='L':
        return 50
    elif c=='C':
        return 100
    elif c=='D':
        return 500
    elif c=='M':
        return 1000
    else:
        print("error")
        return 

#print(rmnlst)

def setrmnc(num):
    if num == 0:
        return ''
    elif num == 1:
        return 'I'
    elif num == 2:
        return 'II'
    elif num == 3:
        return 'III'
    elif num == 4:
        return 'IV'
    elif num == 5:
        return 'V'
    elif num == 6:
        return 'VI'
    elif num == 7:
        return 'VII'
    elif num == 8:
        return 'VIII'
    elif num == 9:
        return 'IX'
    elif num == 10:
        return 'X'
    elif num == 20:
        return 'XX'
    elif num == 30:
        return 'XXX'
    elif num == 40:
        return 'XL'
    elif num == 50:
        return 'L'
    elif num == 60:
        return 'LX'
    elif num == 70:
        return 'LXX'
    elif num == 80:
        return 'LXXX'
    elif num == 90:
        return 'XC'
    elif num == 100:
        return 'C'
    elif num == 200:
        return 'CC'
    elif num == 300:
        return 'CCC'
    elif num == 400:
        return 'CD'
    elif num == 500:
        return 'D'
    elif num == 600:
        return 'DC'
    elif num == 700:
        return 'DCC'
    elif num == 800:
        return 'DCCC'
    elif num == 900:
        return 'CM'
    elif num == 1000:
        return 'M'
    elif num == 2000:
        return 'MM'
    elif num == 3000:
        return 'MMM'
    elif num == 4000:
        return 'MMMM'
    else:
        print("error")
        return
    

def readrmn(rmn):
    lenrmn = len(rmn)
    tot = 0
    for i in range(lenrmn):
        num = getrmnc(rmn[i])
        if i == lenrmn-1:
            tot += num
        else:
            nextnum = getrmnc(rmn[i+1])
            if num>=nextnum:
                tot += num
            else:
                tot -= num
    return tot

   
def writermn(num):
    d4 = num//1000*1000
    d3 = (num-d4)//100*100
    d2 = (num-d4-d3)//10*10
    d1 = num-d4-d3-d2
    rmn = setrmnc(d4) + setrmnc(d3) + setrmnc(d2) + setrmnc(d1)
    return rmn
        

newrmnlst = []
difflen = []
for i in rmnlst:
    num = readrmn(i)
    rmn = writermn(num)
    newrmnlst += [rmn]
    difflen += [len(i) - len(rmn)]    

print(sum(difflen))
        
