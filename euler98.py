from collections import defaultdict
import math

f = open("D:\p098_words.txt", "r")
wordlist = []
for line in f:
    wordlist += line.rstrip("\n").replace('"','').split(",")
f.close()
worddict = defaultdict(list)
for word in wordlist:
    reword = ''.join(sorted(list(word)))
#    print(word,reword)
    worddict[reword] += [word]

worddict2 = dict(filter(lambda e:len(e[1])>1, worddict.items()))

maxlen = max(map(len,worddict2.keys()))

squarelist = [[] for i in range(maxlen+1)]
i = 0
s = 0
while(1):
    i += 1
    s = i*i
    l = int(math.log10(s)) + 1
    if l > maxlen:
        break
    squarelist[l] += [str(s)]


def wordmapnum(word,wordmap):
    wordnum = ''
    for p in range(len(word)):
        # 按照映射表重构word对应的数字，看是否合法
        wordnum += wordmap[word[p]]    
    return wordnum

maxsquare = 0
for wordkey,wordpool in worddict2.items():
    # 从worddict里取出变换的word组
    wordlen = len(wordkey)
    for num in squarelist[wordlen]:
        # 从word长度的平方数中取出一个平方数    
        poollen = len(wordpool)
        for k in range(poollen-1):
        # 从变换的word组里取出一个word
            word = wordpool[k]
            wordmap = {}
            for p in range(wordlen):
                # 对word的每个字幕映射数字
                wordmap[word[p]] = num[p]
            
            if wordmapnum(word,wordmap) != num:
                # 一个字母对应多个数字的情况
                continue
            if len(set(wordmap.values())) < len(set(list(word))):
                # 多个字母对应一个数字的情况
                continue
            for l in range(k+1,poollen):
                word2 = wordpool[l]
                wordnum2 = wordmapnum(word2,wordmap)
                if wordnum2 in squarelist[wordlen]:
                    maxsquare = max(maxsquare,int(num), int(wordnum2))

print(maxsquare)
                
            
                
                
        
