li=[]
for x in range(8):
    a=list(input())
    li.append(a)
dap=0
for x in range(8):
    for y in range(8):
        if (x+y)%2==0 and li[x][y]=='F':
            dap+=1
print(dap)