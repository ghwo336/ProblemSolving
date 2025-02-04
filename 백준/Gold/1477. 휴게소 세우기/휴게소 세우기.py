n,m,l=map(int,input().split())
li=[0,l]+list(map(int,input().split()))
li.sort()
start=1
end=l-1
dap=0
while start<=end:
    cnt=0
    mid=(start+end)//2
    for x in range(1,n+2):
        if li[x]-li[x-1]>mid:
            cnt+=(li[x]-li[x-1]-1)//mid
    if cnt>m:
        start=mid+1
    else:
        end=mid-1
        dap=mid

print(dap)