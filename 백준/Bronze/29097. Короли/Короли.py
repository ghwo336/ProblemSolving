n,m,k,a,b,c=map(int,input().split())
dap=[]
di=dict()
di['Joffrey']=n*a
di['Robb']=m*b
di['Stannis']=k*c
fiv=max(n*a,m*b,k*c)
for x in di:
    if di[x]==fiv:
        dap.append(x)
dap.sort()
print(*dap)