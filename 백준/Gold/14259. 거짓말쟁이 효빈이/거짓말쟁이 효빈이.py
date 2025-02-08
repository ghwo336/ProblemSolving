n,k,a=map(int,input().split())
m=int(input())
li=list(map(int,input().split()))
start=0
end=m
dap=1

while start<=end:
    mid=(start+end)//2
    li2=[0]+li[:mid]+[n+1]
    li2.sort()
    fiv=0
    for x in range(1,mid+2):
        if li2[x]!=li2[x-1]:
            fiv+=((li2[x]-li2[x-1])//(a+1))
    if fiv>=k:
        dap=mid+1
        start=mid+1
    else:
        end=mid-1

if dap>m:
    print(-1)
else:
    print(dap)