from collections import defaultdict



#lastbatch = {((2,3,4,5),):1}
lastbatch= {((2,3,4,5),):1}

for i in range(13):
    batch = defaultdict(int)
    for trace,cnt in lastbatch.items():
        evp = list(trace[-1])
        for j in range(len(evp)):
            newevp = [x for x in evp]
            del newevp[j]
            if evp[j] == 2:
                newevp += [3,4,5]
            elif evp[j] == 3:
                newevp += [4,5]
            elif evp[j] == 4:
                newevp += [5]
            newevp = tuple(sorted(newevp))
            newtrace = trace + (newevp,)
            batch[newtrace] += cnt/len(evp)
    lastbatch = dict(batch)
    
cnt = 0
for k,v in batch.items():
    cnt += sum(v if len(evp) == 1 else 0 for evp in k)

print(cnt)
                
