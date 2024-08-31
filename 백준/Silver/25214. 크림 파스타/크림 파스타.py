N=int(input())
li=list(map(int,input().split()))
dap=[0]
s=li[0]
l=li[0]
for x in range(1,N):
    if l<li[x]:
        l=li[x]
    if s>li[x]:
        s=li[x]
        l=li[x]
    dap.append(max(dap[-1],l-s))
print(*dap)