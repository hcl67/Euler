'''
Project Euler #59

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''
file=open("D:\\Python32\\djinn\\raw\\cipher1.txt")
cipher=file.readline().rstrip('\n').split(',')
# ASCII a-z : 97-122
def find():
    for c in range(97,123):
        for b in range(97,123):
            for a in range(97,123):
                flg=1
                x=a
                y=b
                z=c
                for i in cipher:
                    if (x^int(i)>=32 and x^int(i)<=34) or (x^int(i)>=39 and x^int(i)<=41) or (x^int(i)>=44 and x^int(i)<=59) or x^int(i)==63 or (x^int(i)>=65 and x^int(i)<=90) or (x^int(i)>=97 and x^int(i)<=122):
                        u=x
                        x=y
                        y=z
                        z=u

                    else:
                        flg=0
                        break
                if flg==1:
                    print(a,b,c)
                    return [a,b,c]

def printcipher(s):
    x=s[0]
    y=s[1]
    z=s[2]
    for i in cipher:
        print(chr(x^int(i)),end="")
        u=x
        x=y
        y=z
        z=u

def printsumcipher(s):
    x=s[0]
    y=s[1]
    z=s[2]
    sum=0
    for i in cipher:
        sum+=x^int(i)
        u=x
        x=y
        y=z
        z=u
    print(sum)

    
s=find()
#printcipher(s)
printsumcipher(s)
