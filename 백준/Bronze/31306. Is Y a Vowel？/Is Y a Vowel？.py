a=input()
dap=0
y=0
s={'a','i','e','o','u'}
for x in a:
    if x in s:
        dap+=1
    if x=='y':
        y+=1

print(dap,dap+y)
