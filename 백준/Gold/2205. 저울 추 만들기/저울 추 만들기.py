import math
n=int(input())
visit=[False for _ in range(n+1)]
dap=[]
fiv=2**int(math.log(2*n,2))
for x in range(1,n+1):
    now=n+1-x
    k=fiv
    while True:
        if k-now<=n and not visit[k-now]:
            visit[k-now]=True
            dap.append(k-now)
            break
        else:
            k//=2
dap.reverse()
for x in dap:
    print(x)
        
    
    
    
    
