

thrd = 10**8
#thrd = 1000


def ispalindromic125(n):
    return str(n) == str(n)[::-1]


i = 0
ssum = 0
while 1:
    i += 1
    ssum += i**2
    if ssum > thrd:
        break

ans = []


while i>2:
    ssum -= i**2
    i -= 1
    a = 0
    while 1:
        csum = a*a*i + a*i*(i+1) + ssum
        if csum > thrd:
            break
        if ispalindromic125(csum):
            ans += [(csum,i,a)]
        a += 1

print(sum(set([x[0] for x in ans])))

