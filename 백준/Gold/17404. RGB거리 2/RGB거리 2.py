N=int(input())
lir=[]
lig=[]
lib=[]
for x in range(N):
    a,b,c=(map(int,input().split()))
    lir.append([a,b,c])
    lig.append([a,b,c])
    lib.append([a,b,c])
dap=10000000000000000000
lir[0][1]=dap
lir[0][2]=dap
lig[0][0]=dap
lig[0][2]=dap
lib[0][0]=dap
lib[0][1]=dap

lir[-1][0]=dap
lig[-1][1]=dap
lib[-1][2]=dap

for x in range(1,N):
    lir[x][0]=lir[x][0]+min(lir[x-1][1],lir[x-1][2])
    lir[x][1]=lir[x][1]+min(lir[x-1][0],lir[x-1][2])
    lir[x][2]=lir[x][2]+min(lir[x-1][1],lir[x-1][0])

    lib[x][0]=lib[x][0]+min(lib[x-1][1],lib[x-1][2])
    lib[x][1]=lib[x][1]+min(lib[x-1][0],lib[x-1][2])
    lib[x][2]=lib[x][2]+min(lib[x-1][1],lib[x-1][0])

    lig[x][0]=lig[x][0]+min(lig[x-1][1],lig[x-1][2])
    lig[x][1]=lig[x][1]+min(lig[x-1][0],lig[x-1][2])
    lig[x][2]=lig[x][2]+min(lig[x-1][1],lig[x-1][0])

    
print(min(min(lir[-1]),min(lig[-1]),min(lib[-1])))    