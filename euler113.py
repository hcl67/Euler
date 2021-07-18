
inc = [[1,1,1,1,1,1,1,1,1,1]]
dec = [[1,1,1,1,1,1,1,1,1,1]]

nbc = [sum(inc[0][1:]) + sum(dec[0][1:]) - 9]


k = 100

for i in range(1,k):
    inc += [[sum(inc[i-1][j:]) for j in range(10)]]
    dec += [[sum(dec[i-1][:j+1]) for j in range(10)]]
    nbc += [sum(inc[i][1:]) + sum(dec[i][1:]) - 9]

print(sum(nbc))
