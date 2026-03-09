a=input()
if a[-1]=='0':
    if a=='12345678910':
        print(10)
    else:
        print(-1)
else:
    dap=''
    fiv=int(a[-1])
    for x in range(1,fiv+1):
        dap+=str(x)
    if dap==a:
        print(fiv)
    else:
        print(-1)