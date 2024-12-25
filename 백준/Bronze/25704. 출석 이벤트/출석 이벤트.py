n=int(input())
p=int(input())
dap=p
if n>=5:
    dap=min(dap,p-500)
if n>=10:
    dap=min(dap,p*9//10)
if n>=15:
    dap=min(dap,p-2000)
if n>=20:
    dap=min(dap,p*3//4)

print(max(dap,0))