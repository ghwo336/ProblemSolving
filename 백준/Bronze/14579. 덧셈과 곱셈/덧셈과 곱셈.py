s,e=map(int,input().split())
dap=1

for x in range(s,e+1):
    dap*=((x**2+x)//2)
    dap%=14579
print(dap)