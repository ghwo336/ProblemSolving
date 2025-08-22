a=input()
b=input()
n=len(a)
dap=''
for x in range(n):
    dap+=max(a[x],b[x])
print(dap)