n=int(input())
li=list(map(int,input().split()))
dap=0
for x in range(n):
    a,b=map(int,input().split())
    if li[x]:
        dap+=max(0,b-a)
print(dap)