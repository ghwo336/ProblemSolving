N=int(input())
li=[]
for x in range(N):
    a=int(input())
    li.append(a)
dp=[[0,0,0]]
for x in range(N):
    li2=[]
    li2.append(max(dp[-1][1],dp[-1][2]))
    li2.append(max(dp[-1][0]+li[x],dp[-1][1]))
    li2.append(max(dp[-1][1]+li[x],dp[-1][2]))
    dp.append(li2)
print(max(dp[-1]))
    