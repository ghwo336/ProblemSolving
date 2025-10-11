while True:
    n=int(input())
    if n==0:
        break
    dap=0
    li=list(map(int,input().split()))
    for x in range(n-2):
        dap=max(dap,li[x]+li[x+1]+li[x+2])
    print(dap)
    