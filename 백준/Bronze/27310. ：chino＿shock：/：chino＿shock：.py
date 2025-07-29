a=input()
dap=len(a)
for x in a:
    if x==':':
        dap+=1
    if x=='_':
        dap+=5
print(dap)