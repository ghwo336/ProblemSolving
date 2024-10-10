# [1,2]
# [3,4]
# [7,10]
# [17,24]
N=int(input())
dp=[[0,0],[1,2]]
for x in range(N-1):
    li=[]
    li.append((sum(dp[-1]))%9901)
    li.append((dp[-1][0]*2+dp[-1][1])%9901)
    dp.append(li)
print(sum(dp[-1])%9901)