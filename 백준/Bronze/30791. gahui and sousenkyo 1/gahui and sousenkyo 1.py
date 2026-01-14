li=list(map(int,input().split()))
dap=0
for x in range(1,5):
    if li[0]-li[x]<=1000:
        dap+=1

print(dap)