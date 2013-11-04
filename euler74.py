'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
def factorial(n):
    n=int(n)
    if n<=0:
        return 1
    else:
        r=1
        while n>1:
            r*=n
            n-=1
        return r

f=[factorial(i) for i in range(10)]

MIN=1
MAX=1000000
n60=0
for i in range(MIN,MAX+1):
    l=[i]
    while 1:
        ln=sum([f[int(c)] for c in str(l[-1])])
        if ln in l:
            #print(l)
            if len(l)>=60:
                n60+=1
            break
        else:
            l.append(ln)
    if i%10000==0:
        print(i)
        print(n60)
print(n60)
        
        
