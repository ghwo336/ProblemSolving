a=input()
dap=1
now=1
for x in range(1,len(a)):
    if a[x]>a[x-1]:
        now+=1
        dap+=now
    else:
        now=1
        dap+=now
print(dap)