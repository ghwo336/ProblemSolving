import math
n=int(input())
che=[True for _ in range(n+1)]
for x in range(2,n+1):
    if che[x]:
        for y in range(x*2,n+1,x):
            che[y]=False

dap=0
while n!=1:
    for x in range(2,n+1):
        if n%x==0:
            n//=x
            dap+=1
            break
pandan=1
realdap=0
while dap>pandan:
    pandan*=2
    realdap+=1
print(realdap)
            
            