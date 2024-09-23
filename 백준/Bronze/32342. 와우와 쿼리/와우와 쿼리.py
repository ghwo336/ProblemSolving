N=int(input())
for x in range(N):
    a=input()
    dap=0
    if len(a)<3:
        print(0)
    else:
        for x in range(len(a)-2):
            if a[x]=='W' and a[x+1]=='O' and a[x+2]=='W':
                dap+=1
        print(dap)