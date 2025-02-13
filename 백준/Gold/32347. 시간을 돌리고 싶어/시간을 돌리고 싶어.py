def pandan(day,k):
    global n;
    now=n-1
    p=False
    while True:
        if k==0:
            break
        if now-day <= 0:
            p=True
            return True
        for x in range(now-day,now):
            if li[x]==1:
                now=x
                k-=1
                break
        else: return False
    return False
        

n,k=map(int,input().split())

li=list(map(int,input().split()))
start=1
end=n-1
dap=1000000000000

while start<=end:
    mid=(start+end)//2
    if pandan(mid,k):
        end=mid-1
        dap=min(dap,mid)
    else:
        start=mid+1
print(dap) 