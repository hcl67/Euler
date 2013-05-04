'''
Project Euler Problem #54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD 	    2C 3S 8S 8D TD      	Player 2
                Pair of Eights      Pair of Fives
2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH	        Player 1
                Highest card Ace    Highest card Queen
3	 	2D 9C AS AH AC      3D 6D 7D TD QD 	        Player 2	 	
                Three Aces          Flush with Diamonds
4	 	4D 6S 9H QH QC 	    3D 6D 7H QD QS 	        Player 1
                Pair of Queens      Pair of Queens
                Highest card Nine   Highest card Seven
5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D 	        Player 1
                Full House          Full House
                With Three Fours    with Three Threes
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
def fmtz(i,n):
    k=str(i)
    if len(k)>=n:
        return k
    else:
        while len(k)<n:
            k='0'+k
        return k

def pokercheck(p):
    n1=[i[:-1] for i in p]
    n1n=[]
    n2=[i[-1] for i in p]
    for i in n1:
        if i=='T':
            n1n.append(10)
        elif i=='J':
            n1n.append(11)
        elif i=='Q':
            n1n.append(12)
        elif i=='K':
            n1n.append(13)
        elif i=='A':
            n1n.append(14)
        else:
            n1n.append(int(i))
    if len(set(n2))==1:
        flush=1
    else:
        flush=0
    n1n.sort(reverse=True)
    n1s=[fmtz(i,2) for i in n1n]
    if len(set(n1s))==5:
        if int(n1s[0])-4!=int(n1s[-1]) and flush==0:
            return int('1'+''.join(n1s))
        elif int(n1s[0])-4==int(n1s[-1]) and flush==0:
            return int('5'+''.join(n1s))
        elif int(n1s[0])-4!=int(n1s[-1]) and flush==1:
            return int('6'+''.join(n1s))            
        elif int(n1s[0])-4==int(n1s[-1]) and flush==1:
            return int('9'+''.join(n1s))
        else:
            return 0
    elif len(set(n1s))==4:
        for i in range(4):
            if n1s[i]==n1s[i+1]:
                k2=i
                break
        return int('2'+''.join(n1s[k2:k2+2]+n1s[:k2]+n1s[k2+2:]))
    elif len(set(n1s))==3:
        k3=-1
        for i in range(3):
            if n1s[i]==n1s[i+1] and n1s[i+1]==n1s[i+2]:
                k3=i
                break
        if k3>=0:
            return int('4'+''.join(n1s[k3:k3+3]+n1s[:k3]+n1s[k3+3:]))
        else:
            if n1s[0]==n1s[1]:
                k21=0
            else:
                k21=1
            if n1s[3]==n1s[4]:
                k22=3
            else:
                k22=2
            return int('3'+''.join(n1s[k21:k21+2]+n1s[k22:k22+2]+n1s[:k21]+n1s[k21+2:k22]+n1s[k22+2:]))
    elif len(set(n1s))==2:
        k4=-1
        for i in range(2):
            if n1s[i]==n1s[i+1] and n1s[i+1]==n1s[i+2] and n1s[i+2]==n1s[i+3]:
                k4=i
                break
        if k4>=0:
            return int('8'+''.join(n1s[k4:k4+4]+n1s[:k4]+n1s[k4+4:]))
        else:
            if n1s[1]==n1s[2]:
                k3=0
            else:
                k3=2
            return int('7'+''.join(n1s[k3:k3+3]+n1s[:k3]+n1s[k3+3:]))
    else:
        return 0

win1=0
pokerfile=open("D:\\Python32\\djinn\\raw\\poker.txt")
for line in pokerfile:
    poker=line.rstrip('\n').split(' ')
    if pokercheck(poker[:5])>pokercheck(poker[5:]):
        win1+=1
print(win1)
 














