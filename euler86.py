import math,datetime

# begintime = datetime.datetime.now()
# cnt = 0
# for a in range(1, 501):
#     for b in range(1,a+1):
#         for c in range(1,b+1):
#             i = math.sqrt(a*a + (b+c) * (b+c))
#             if i == int(i):
#                 cnt += 1
# #                print(a,b,c)
# print(cnt)
# print(datetime.datetime.now() - begintime)

begintime = datetime.datetime.now()
cnt = 0
for a in range(1, 3001):
    for b in range(2,2*a+1):
        i = math.sqrt(a*a+b*b)
        if i == int(i):
            cnt += (min(2*a-b+1,b-1)+1)//2
        if cnt > 1000000:
            break
    if cnt > 1000000:
        break
#            print(a,b)
print(cnt)
print(a)
print(datetime.datetime.now() - begintime)
