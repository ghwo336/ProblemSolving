n,m=map(int,input().split())
dap=n
while n//m!=0:
    n//=m
    dap+=n    
print(dap)