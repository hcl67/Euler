import math
f = open("p102_triangles.txt", "r")
ordlist = []
for line in f:
    ordlist += [list(map(int,line.rstrip("\n").split(",")))]
f.close()


def calangle(x,y):
    angle = math.atan2(y,x)
    if angle < 0:
        angle += math.pi * 2
    return angle

ans = []
for ordi in ordlist:
    angle1 = calangle(ordi[0],ordi[1])
    angle2 = calangle(ordi[2],ordi[3])
    angle3 = calangle(ordi[4],ordi[5])
    angleb1 = angle1 + math.pi
    if angleb1 > math.pi*2:
        angleb1 -= math.pi*2
    angleb2 = angle2 + math.pi
    if angleb2 > math.pi*2:
        angleb2 -= math.pi*2        
    
    minangle = min(angleb1,angleb2)
    maxangle = max(angleb1,angleb2)
    if maxangle - minangle <= math.pi:
        if angle3 >= min(angleb1,angleb2) and angle3 <= max(angleb1,angleb2):
            ans += [1]
        else:
            ans += [0]
    else:
        if angle3 < min(angleb1,angleb2) or angle3 > max(angleb1,angleb2):
            ans += [1]
        else:
            ans += [0]        
        
print(sum(ans))
    
    
