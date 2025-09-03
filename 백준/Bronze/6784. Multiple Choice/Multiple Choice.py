n=int(input())
li=[]
dap=[]
for x in range(n):
    li.append(input())
for x in range(n):
    dap.append(input())
d=0
for x in range(n):
    if li[x]==dap[x]:
        d+=1
print(d)