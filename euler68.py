'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

'''

'''
sum of each line from 14 to 19
'''
def Permutate(l):
    if len(l)==1:
        return [l]
    else:
        returnlist=[]
        for i in range(len(l)):
            t=[x for x in l]
            t.pop(i)
            p=Permutate(t)
            for j in p:
                returnlist+=[[l[i]]+j]
        return returnlist


#f=Permutate([1,2,3,4,5,6,7,8,9,10])
#full=Permutate(['1','2','3','4','5','7','8','9','10'])
full=Permutate(['1','2','3','4','5','7','8','9','10'])

l_r=[]
for f in full:
    f=['6']+f
    if f.index('10')>=5 or f.index('9')>=5 or f.index('8')>=5 or f.index('7')>=5:
        continue
    l1=[f[0],f[5],f[6]]
    sl1=int(l1[0])+int(l1[1])+int(l1[2])
    if sl1>19 or sl1<14:
        continue
    l2=[f[1],f[6],f[7]]
    sl2=int(l2[0])+int(l2[1])+int(l2[2])
    if sl2>19 or sl2<14 or sl2!=sl1:
        continue
    l3=[f[2],f[7],f[8]]
    sl3=int(l3[0])+int(l3[1])+int(l3[2])
    if sl3>19 or sl3<14 or sl3!=sl1:
        continue
    l4=[f[3],f[8],f[9]]
    sl4=int(l4[0])+int(l4[1])+int(l4[2])
    if sl4>19 or sl4<14 or sl4!=sl1:
        continue
    l5=[f[4],f[9],f[5]]
    sl5=int(l5[0])+int(l5[1])+int(l5[2])
    if sl5>19 or sl5<14 or sl5!=sl1:
        continue
    r=''.join(l1+l2+l3+l4+l5)
    print(r)
    l_r.append(r)
print(sorted(l_r))
    
    
