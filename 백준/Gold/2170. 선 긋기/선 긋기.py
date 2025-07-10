n=int(input())
li=[]
for x in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort()
dap=0
start=li[0][0]
end=li[0][1]
for x in range(1,n):
    if li[x][0]>end:
        dap+=(end-start)
        start=li[x][0]
        end=li[x][1]
    else:
        end=max(li[x][1],end)
dap+=(end-start)
print(dap)
    