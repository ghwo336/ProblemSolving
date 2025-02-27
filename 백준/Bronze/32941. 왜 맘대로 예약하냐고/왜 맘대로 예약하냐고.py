t,x=map(int,input().split())
s=set()
dap=[0 for _ in range(t+1)]
n=int(input())
for _ in range(n):
    a=int(input())
    li=list(map(int,input().split()))
    for i in li:
        dap[i]+=1

if dap[x]==n:
    print("YES")
else:
    print("NO")
        