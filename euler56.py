'''
Product Euler Problem #56

A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b<100, what is the maximum digital sum?
'''
def sumdigit(i):
    si=list(str(i))
    s=0
    while len(si)>0: s+=int(si.pop())
    return s

md=0
for i in range(100):
    for j in range(100):
        md=max(sumdigit(i**j),md)
print(md)
            
