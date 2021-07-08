import datetime

btime = datetime.datetime.now()

BIGN = 1000000000000
k = 3
n = 4

while(n<BIGN):
    newk = 3*k+2*n-2
    newn = 4*k+3*n-3
    k = newk
    n = newn
        
print(k)        
print(datetime.datetime.now()-btime)


'''
k =  3 n =  4
k =  15 n =  21
k =  85 n =  120
k =  493 n =  697
k =  2871 n =  4060
k =  16731 n =  23661
k =  97513 n =  137904
k =  568345 n =  803761
k =  3312555 n =  4684660
k =  19306983 n =  27304197
k =  112529341 n =  159140520
推算的通项公式
k[i] = 3*k[i-1]+2*n[i-1]-2
n[i] = 4*k[i-1]+3*n[i-1]-3
'''    
