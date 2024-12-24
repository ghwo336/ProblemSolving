li=list(map(int,input().split()))
li2=list(map(int,input().split()))
dap=0
for x in range(3):
    if li2[x]>li[x]:
        dap+=(li2[x]-li[x])
print(dap)