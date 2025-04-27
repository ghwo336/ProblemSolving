n,m=map(int,input().split())
li=list(map(int,input().split()))
user=[]
bad=[0 for _ in range(n)]
for x in range(n-1):
    li2=list(map(int,input().split()))
    user.append(li2)
    pandan=0
    for y in range(m):
        pandan+=abs(li2[y]-li[y])
    if pandan>2000:
        bad[x]=1
if n-1-sum(bad)<=sum(bad):
    print("YES")
else:
    print("NO")
        
        
