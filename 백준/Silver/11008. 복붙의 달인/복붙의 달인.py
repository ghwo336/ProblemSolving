t=int(input())
for _ in range(t):
    a,b=input().split()
    n=len(a)
    fn=len(b)
    dap=0
    now=0
    while now+fn<=n:
        fiv=1
        for x in range(fn):
            if a[now+x]!=b[x]:
                fiv=0
                break
        if fiv:
            dap+=1
            now+=fn
        else:
            now+=1
    print(n-dap*(fn-1))
        
    