a,b,c=map(int,input().split(' : '))
d,e,f=map(int,input().split(' : '))
dap=3600*(d-a)+60*(e-b)+f-c
if dap<0:
    print(dap+3600*24)
else:
    print(dap)