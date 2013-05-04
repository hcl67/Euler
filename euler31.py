'''
Project Euler Problem #31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can £2 be made using any number of coins?
'''
p=[]
c=0
for i1 in range(2):
    for i2 in range((200-200*i1)//100+1):
        for i3 in range((200-200*i1-100*i2)//50+1):
            for i4 in range((200-200*i1-100*i2-50*i3)//20+1):
                for i5 in range((200-200*i1-100*i2-50*i3-20*i4)//10+1):
                    for i6 in range((200-200*i1-100*i2-50*i3-20*i4-10*i5)//5+1):
                        for i7 in range((200-200*i1-100*i2-50*i3-20*i4-10*i5-5*i6)//2+1):
                            p.append([i1,i2,i3,i4,i5,i6,i7])
                            c+=1
print(c)
                    
                        
                    
