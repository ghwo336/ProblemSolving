a=input()
if len(a)<4:
    print(0)
else:
    dap=0
    for x in range(len(a)-3):
        if a[x]== 'D' and a[x+1]=='K' and a[x+2]=='S' and a[x+3]=='H':
            dap+=1
    print(dap)
        