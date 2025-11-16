n=int(input())
for x in range(n):
    a=(input())
    dap1=0
    for y in a:
        dap1+=int(y)
    dap2=int(a[-3:])*10
    dap3=(dap1+dap2)%10000
    if (dap1+dap2)<1000:
        print(dap1+dap2+1000)
    else:
        if len(str(dap3))==4:
            print((dap3))
        else:
            dap3=str(dap3)
            while len(dap3)!=4:
                dap3='0'+dap3
            print(dap3)
    