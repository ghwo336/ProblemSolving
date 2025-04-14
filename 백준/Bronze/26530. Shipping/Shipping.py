t=int(input())
for x in range(t):
    n=int(input())
    dap=0
    for y in range(n):
        li=list(input().split())
        dap+=float(li[1])*float(li[2])
    print(f"${dap:.2f}")