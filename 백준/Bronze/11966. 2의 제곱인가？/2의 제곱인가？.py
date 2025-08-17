n=int(input())
dap=0
fiv=1
for x in range(31):
    if n==fiv:
        dap=1
    fiv*=2
print(dap)
    