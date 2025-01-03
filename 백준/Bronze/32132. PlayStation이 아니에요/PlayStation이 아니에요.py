def sol():
    n=int(input())
    s=input()
    dap=''
    if n<=2:
        print(s)
        return;
    dap+=(s[0]+s[1])
    for x in range(2,n):
        if not ((s[x]=='4'or s[x]=='5') and dap[-1]=='S' and dap[-2]=='P'):
            dap+=s[x]
    print(dap)
sol()
