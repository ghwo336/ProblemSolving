a,b,c=map(int,input().split())
dap=0
f=(a+b+c)//3
dap+=abs(f-a)
dap+=abs(f-c)
print(dap)