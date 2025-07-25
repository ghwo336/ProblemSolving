t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    dap=b
    for y in range(a-1):
        b+=c
        dap+=b
    print(dap)