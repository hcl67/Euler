'''
Project Euler Problem #36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
plst=[]
for i in range(1,1000000):
    s=str(i)
    if s[::-1]==s:
        b=bin(i)[2:]
        if b[::-1]==b:
            plst.append(i)
print(sum(plst))
            
