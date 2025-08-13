t=int(input())
for x in range(t):
    dap=0
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    for y in li:
        dap+=(y//k)
    print(dap)