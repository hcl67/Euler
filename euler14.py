'''
Project Euler Problem #14

The following iterative sequence is defined for the set of positive integers:

n->n/2 (n is even)
n->3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13->40->20->10->5->16->8->4->2->1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


lendic={1:1}
for i in range(2,1000000):
    if i in lendic:
        continue
    n=[i]
    while 1:
        if n[-1]%2==0:
            n.append(n[-1]//2)
        else:
            n.append(n[-1]*3+1)
        if n[-1] in lendic:
            for i in range(len(n)-1):
                lendic[n[i]]=lendic[n[-1]]+len(n)-1-i
            break
    #print(n)
maxlen=max(lendic.values())
for i in lendic:
    if lendic[i]==maxlen:
        print(i)
        break

