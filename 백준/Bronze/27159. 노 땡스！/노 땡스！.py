n=int(input())
li=list(map(int,input().split()))

dap=li[0]
for x in range(1,n):
    if li[x]-li[x-1]!=1:
        dap+=li[x]
print(dap)