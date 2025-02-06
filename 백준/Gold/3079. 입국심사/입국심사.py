n,m=map(int,input().split())
t=[]
for x in range(n):
    a=int(input())
    t.append(a)
t.sort()
start=1
end=10**18+1
dap=0
while start<=end:
    mid=(start+end)//2
    fiv=0
    for x in t:
        fiv+=mid//x
    if fiv>=m:
        dap=mid
        end=mid-1
    else:
        start=mid+1
print(dap)   
