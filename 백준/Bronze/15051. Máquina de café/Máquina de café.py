dap=1000000000000000000
li=[]
for x in range(3):
    a=int(input())
    li.append(a)
for x in range(3):
    hubo=0
    for y in range(3):
        hubo+=abs(y-x)*li[y]
    dap=min(dap,hubo)
print(dap*2)