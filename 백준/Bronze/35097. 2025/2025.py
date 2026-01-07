while True:
    a=int(input())
    if a==0:
        break
    dap=0
    for x in range(1,a+1):
        for y in range(1,a+1):
            dap+=(x*y)
    print(dap)