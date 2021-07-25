  
__f = open("D:\prime100000.txt", "r")
__plist = []
for line in __f:
    __plist += list(map(int,line.rstrip("\n").split(" ")))
__f.close()

def isprime(n):
    if n == 1:
        return False
    for p in __plist:
        if p*p>n:
            break
        elif n%p == 0:
            return False
    return True

'''

 n^3+n^2*p = k^3
=n^2*(n+p)

若 n != a^3 => n+p = n*a^3 => p=n*(a-1)(a^2+a+1) => n=1，a=2, p=7
故 n = a^3 => n+p = b^3 => p = (b-a)(a^2+ab+b^2) => p = 3*a^2+3*a+1

'''




thrd = 1000000

plist = [7]

a = 1
while 1:
    a+=1
    p = 3*a*a+3*a+1
    if p>thrd:
        break
    if isprime(p):
        print(a**3,p)
        plist += [p]
        
print(len(plist))
