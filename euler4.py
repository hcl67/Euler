'''
Project Euler Problem #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def check():
    for i in range(1,1000):
        for j in range(i):
            x1=999-j
            x2=999-i+1+j
            y=str(x1*x2)
            if y==y[::-1]:
                print("%d x %d = %s" %(x1, x2, y))
                return                 
check()
