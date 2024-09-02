h,y=map(int,input().split())
dp=[h]
for x in range(1,y+1):
    if x>=1:
        dp.append(int(dp[-1]*(1.05)))
    if x>=3:
        if dp[-4]*1.2>dp[-1]:
            dp[-1]=int(dp[-4]*1.2)
    if x>=5:
        if dp[-6]*1.35>dp[-1]:
            dp[-1]=int(dp[-6]*1.35)
print(int(dp[-1]))
