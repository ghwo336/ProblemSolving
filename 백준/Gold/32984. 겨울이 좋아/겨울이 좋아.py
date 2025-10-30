n=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li=[]
for x in range(n):
    if li1[x]%li2[x]==0:
        li.append(li1[x]//li2[x])
    else:
        li.append(li1[x]//li2[x]+1)
li.sort()
start=1
end=li[-1]
dap=1000000000000000000000000
while start<=end:
    mid=(start+end)//2
    fiv=0
    for x in li:
        if x>mid:
            fiv+=(x-mid)
    if fiv<=mid:
        dap=min(dap,mid)
        end=mid-1
    else:
        start=mid+1
print(dap)