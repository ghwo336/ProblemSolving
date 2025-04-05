n=int(input())
dap=0
for x in range(1,n+1):
    m=str(x)
    fiv=1
    for y in m:
        if y!='4' and y!='7':
            fiv=0
            break
    if fiv:
        dap=x


print(dap)