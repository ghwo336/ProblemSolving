x,k=map(int,input().split())
x=list(bin(x)[2:])
k=list(bin(k)[2:])
dap=""
while len(k)!=0:
    if x:
        now=x.pop()
        if now=='1':
            dap+='0'
        else:
            dap+=k.pop()
    else:
        dap+=k.pop()
print(int('0b'+dap[::-1],2))
