fivli=[50,60,70]
while True:
    li=list(map(int,input().split()))
    if len(li)==1 and li[0]==0:
        break
    li=li[1:]
    s=sum(li)
    li.sort()
    big=li[-1]
    dap=[]
    for x in fivli:
        if x<2*s:
            dap.append(0)
        else:
            dap.append(1+x//big)
    print(*dap)