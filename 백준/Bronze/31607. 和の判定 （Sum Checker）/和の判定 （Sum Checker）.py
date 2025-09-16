li=[]
for x in range(3):
    li.append(int(input()))
dap=0
for x in li:
    if x*2==sum(li):
        dap=1
print(dap)