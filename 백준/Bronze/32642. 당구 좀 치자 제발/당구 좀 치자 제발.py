n=int(input())
li=list(map(int,input().split()))
dap=[0]
for x in range(n):
    if li[x]:
        dap.append(dap[-1]+1)
    else:
        dap.append(dap[-1]-1)

print(sum(dap))