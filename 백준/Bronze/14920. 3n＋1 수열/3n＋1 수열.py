n=int(input())
dap=1
while n!=1:
    if n%2==0:
        n//=2
        dap+=1
    else:
        n=n*3+1
        dap+=1
print(dap)