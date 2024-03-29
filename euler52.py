'''
Project Euler Problem #52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def digitcomp(a,b):
    return ''.join(sorted(list(str(a)))) == ''.join(sorted(list(str(b))))

n=9
while 1:
    if digitcomp(n,2*n) and digitcomp(n,3*n)  and digitcomp(n,4*n) and digitcomp(n,5*n) and digitcomp(n,6*n):
        print(n)
        break
    n+=9
    
