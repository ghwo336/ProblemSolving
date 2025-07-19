n=int(input())
li=[]
for x in range(n):
    a=input()
    li.append(a)
l=len(li[0])
dap=''
for x in range(l):
    fiv=li[0][x]
    pandan=True
    for y in li:
        if y[x]!=fiv:
            pandan=False
    if pandan:
        dap+=fiv
    else:
        dap+='?'
print(dap)
