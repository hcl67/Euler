'''
Project Euler Problem #38

Take the number 192 and multiply it by each of 1, 2, and 3:

192*1 = 192
192*2 = 384
192*3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n>1?
'''

for i in range(9999,9000,-1):
    k=list(set(str(i*100002)))
    l=[int(i) for i in k]
    if sum(l)==45:
        r=i
        break
if r*100002>918273645:
    print(r*100002)
else:
    print(918273645)
