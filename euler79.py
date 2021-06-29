list = ['319','680','180','690','129','620','762','689','762','318','368','710','720','710','629','168','160','689','716','731','736','729','316','729','729','710','769','290','719','680','318','389','162','289','162','718','729','319','790','680','890','362','319','760','316','729','380','319','728','716']

nodes = []
edges = []

for seq in list:
    if seq[:2] not in edges:
        edges.append(seq[:2])
    if seq[1:] not in edges:
        edges.append(seq[1:])
    if seq[0] not in nodes:
        nodes.append(seq[0])
    if seq[1] not in nodes:
        nodes.append(seq[1])
    if seq[2] not in nodes:
        nodes.append(seq[2])


#print(len(edges))
print(edges)
#print(len(nodes))
#print(nodes)


edgeout = {n:[] for n in nodes}
edgein = {n:[] for n in nodes}

for e in edges:
    edgeout[e[0]] += e[1]
    edgein[e[1]] += e[0]
    
#print(edgeout)
#print(edgein)

dgout = {n:len(edgeout[n]) for n in edgeout.keys()}
dgin = {n:len(edgein[n]) for n in edgein.keys()}

#print(dgout)
#print(dgin)

check = {n:dgin[n] for n in dgin.keys()}
trial = []
while(0 in check.values()):
    checkq = [n for n in check.keys() if check[n] == 0]
#    print(checkq)
    for n in checkq:
        del check[n]
        trial.append(n)
        for nn in edgein.keys():
            if n in edgein[nn]:
                check[nn] -= 1
#    print(check)

if len(check) == 0:
    print("无环")
else:
    print("有环")
#print(check)
# check circle

print("".join(trial))


