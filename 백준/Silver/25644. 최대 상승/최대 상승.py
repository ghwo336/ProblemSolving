n=int(input())
li=list(map(int,input().split()))
dp=[0]
buy=10**10
for x in li:
    if x<buy:
        buy=x
    else:
        dp.append(x-buy)
print(max(dp))