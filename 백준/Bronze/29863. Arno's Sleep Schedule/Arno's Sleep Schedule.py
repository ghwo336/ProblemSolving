a=int(input())
b=int(input())
dap=0
while (a!=b):
    a+=1
    dap+=1
    if a==24:
        a=0
print(dap)