n=int(input())
dap=0
for x in range(1,n+1):
    s=str(x)
    fiv=0
    for y in s:
        fiv+=int(y)
    if x%fiv==0:
        dap+=1
print(dap)