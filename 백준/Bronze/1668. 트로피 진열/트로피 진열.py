li=[]
n=int(input())
for x in range(n):
    a=int(input())
    li.append(a)
dap1=0
fiv=-1
for x in range(n):
    if li[x]>fiv:
        dap1+=1
        fiv=li[x]
print(dap1)
li.reverse()
dap2=0
fiv=-1
for x in range(n):
    if fiv<li[x]:
        dap2+=1
        fiv=li[x]
print(dap2)