di={'1':2,'0':4}
while True:
    a=input()
    if a=='0':
        break
    dap=len(a)-1
    for x in a:
        if x in di:
            dap+=di[x]
        else:
            dap+=3
    print(dap+2)