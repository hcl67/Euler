'''
Project Euler Problem #17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


1:one:3
2:two:3
3:three:5
4:four:4
5:five:4
6:six:3
7:seven:5
8:eight:5
9:nine:4
10:ten:3
11:eleven:6
12:twelve:6
13:thirteen:8
14:fourteen:8
15:fifteen:7
16:sixteen:7
17:seventeen:9
18:eighteen:8
19:nineteen:8
20:twenty:6
30:thirty:6
40:forty:5
50:fifty:5
60:sixty:5
70:seventy:7
80:eighty:6
90:ninety:6
100:hundred:7
1000:thousand:8


'''
def transnum(x):
    numdic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
    if x<=99 and x in numdic:
        return numdic[x]
    elif x<100:
        return numdic[x//10*10]+' '+numdic[x%10]
    elif x==1000:
        return numdic[x//1000]+' '+numdic[1000]
    elif x%100==0:
        return numdic[x//100]+' '+numdic[100]
    else:
        return numdic[x//100]+' '+numdic[100]+' and '+transnum(x%100)



s=0
for i in range(1,1001):
    s=s+len(transnum(i))-transnum(i).count(' ')
print(s)

