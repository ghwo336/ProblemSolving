n,k,m=map(int,input().split())
now=0
m-=1

for dap in range(1,n+1):
    delete= (now+k-1)%n
    if delete==m:
        print(dap)
        break
    elif delete<m:
        m-=1
    n-=1    
    now=delete
    